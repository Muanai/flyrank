import os
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from dotenv import load_dotenv

from auth import supabase
from schemas import AuthCredentials, SignupResponse, LoginResponse, ErrorResponse

load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("auth-api")

@asynccontextmanager
async def lifespan(app: FastAPI):
    if supabase is not None:
        logger.info("Server running and connected to Supabase")
    else:
        logger.warning("Supabase client not initialized! Please verify SUPABASE_KEY in .env")
    yield

app = FastAPI(
    title="Auth - Login & Protect API",
    description="Secure Authentication & Protected Routes using Supabase Auth and FastAPI",
    version="1.0.0",
    lifespan=lifespan,
)

# Custom validation exception handler: ensure 400 Bad Request on missing/invalid input
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    missing_fields = [str(err.get("loc", [""])[-1]) for err in errors if "missing" in str(err.get("type"))]
    if missing_fields:
        err_msg = f"Missing required field(s): {', '.join(missing_fields)}"
    else:
        err_msg = "Invalid request input format"
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"error": err_msg, "details": errors}
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    if isinstance(exc.detail, dict) and "error" in exc.detail:
        return JSONResponse(status_code=exc.status_code, content=exc.detail)
    return JSONResponse(status_code=exc.status_code, content={"error": str(exc.detail)})

@app.get("/", tags=["Health"])
def root():
    return {
        "status": "online",
        "message": "Server running and connected to Supabase",
        "docs": "/docs"
    }

# -------------------------------------------------------------
# Stage 1: Open Auth (Sign Up & Log In)
# -------------------------------------------------------------

@app.post(
    "/auth/signup",
    status_code=status.HTTP_201_CREATED,
    tags=["Authentication"],
    summary="Sign Up a new user",
    responses={
        201: {"description": "User created successfully"},
        400: {"model": ErrorResponse, "description": "Validation or Registration error"}
    }
)
async def signup(credentials: AuthCredentials):
    if not credentials.email or not credentials.email.strip():
        return JSONResponse(status_code=400, content={"error": "Email is required and cannot be empty"})
    if not credentials.password or not credentials.password.strip():
        return JSONResponse(status_code=400, content={"error": "Password is required and cannot be empty"})

    if supabase is None:
        return JSONResponse(status_code=500, content={"error": "Supabase client not configured"})

    try:
        res = supabase.auth.sign_up({
            "email": credentials.email.strip(),
            "password": credentials.password
        })
        if not res.user:
            return JSONResponse(status_code=400, content={"error": "Registration failed"})

        user_data = {
            "id": res.user.id,
            "email": res.user.email,
            "created_at": str(res.user.created_at) if hasattr(res.user, "created_at") else None,
            "app_metadata": getattr(res.user, "app_metadata", {}),
            "user_metadata": getattr(res.user, "user_metadata", {})
        }
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message": "User registered successfully", "user": user_data}
        )
    except Exception as e:
        logger.error(f"Signup error: {e}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": str(e)}
        )

@app.post(
    "/auth/login",
    status_code=status.HTTP_200_OK,
    tags=["Authentication"],
    summary="Authenticate user and return JWT access token",
    responses={
        200: {"model": LoginResponse, "description": "Login successful"},
        400: {"model": ErrorResponse, "description": "Missing credentials"},
        401: {"model": ErrorResponse, "description": "Invalid login credentials"}
    }
)
async def login(credentials: AuthCredentials):
    if not credentials.email or not credentials.email.strip():
        return JSONResponse(status_code=400, content={"error": "Email is required and cannot be empty"})
    if not credentials.password or not credentials.password.strip():
        return JSONResponse(status_code=400, content={"error": "Password is required and cannot be empty"})

    if supabase is None:
        return JSONResponse(status_code=500, content={"error": "Supabase client not configured"})

    try:
        res = supabase.auth.sign_in_with_password({
            "email": credentials.email.strip(),
            "password": credentials.password
        })
        if not res.session or not res.session.access_token:
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"error": "Invalid login credentials"})

        user = res.user or res.session.user
        if not user:
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"error": "Invalid login credentials"})

        return {
            "access_token": res.session.access_token,
            "token_type": "bearer",
            "refresh_token": res.session.refresh_token,
            "user": {
                "id": user.id,
                "email": user.email,
                "created_at": str(user.created_at) if hasattr(user, "created_at") else None
            }
        }
    except Exception as e:
        logger.warning(f"Login failed: {e}")
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"error": "Invalid login credentials"}
        )

# -------------------------------------------------------------
# Stage 2: The Public & Protected Gates
# -------------------------------------------------------------

@app.get(
    "/public/info",
    status_code=status.HTTP_200_OK,
    tags=["Public"],
    summary="Read public, unprotected data"
)
async def public_info():
    return {"message": "Welcome stranger! This info is public."}

@app.get(
    "/protected/profile",
    status_code=status.HTTP_200_OK,
    tags=["Protected"],
    summary="Read private user profile data (Verified token check)"
)
async def protected_profile(request: Request):
    auth_header = request.headers.get("Authorization")
    
    if not auth_header:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"error": "Access token required"}
        )
    
    parts = auth_header.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"error": "Access token required"}
        )
    
    token = parts[1]
    if supabase is None:
        return JSONResponse(status_code=500, content={"error": "Supabase client not configured"})

    # Stage 3: Verify the token with Supabase
    try:
        res = supabase.auth.get_user(token)
        if not res or not res.user:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"error": "Invalid or expired token"}
            )
            
        user = res.user
        return {
            "message": "Token verified successfully!",
            "user": {
                "id": user.id,
                "email": user.email,
                "created_at": str(user.created_at) if hasattr(user, "created_at") else None
            }
        }
    except Exception as e:
        logger.warning(f"Token verification failed: {e}")
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"error": "Invalid or expired token"}
        )

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
