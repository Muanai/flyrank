import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

if not SUPABASE_URL or not SUPABASE_KEY or "PASTE_YOUR_ANON_KEY_HERE" in SUPABASE_KEY:
    # Notice: SUPABASE_KEY should be provided in .env
    pass

def get_supabase_client() -> Client:
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY must be configured in .env")
    return create_client(SUPABASE_URL, SUPABASE_KEY)

try:
    supabase: Client | None = get_supabase_client()
except Exception as e:
    supabase = None  # Will be initialized when keys are properly populated
