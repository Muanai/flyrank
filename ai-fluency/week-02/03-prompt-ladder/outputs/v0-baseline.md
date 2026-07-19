# The Prompt Ladder

## Task Overview

### Original Task
Write a portfolio description for my credit risk feature engineering project.

### Objective
Generate a portfolio description that communicates the value of my credit risk project.

### Why This Task Was Selected
This task was selected because portfolio writing requires balancing technical details, engineering decisions, and business impact. It is a real task from my AI engineering portfolio rather than a synthetic example, allowing the prompt iteration process to demonstrate how different prompting layers influence the quality and relevance of AI-generated content.

---

# Version 0 — Baseline

## Layer Applied
None (baseline prompt)

## Prompt
```text
Write a portfolio description for my credit risk project.
```

## Output
```text
I'll read your credit risk project details first, then craft a compelling portfolio description.

Here's a polished portfolio description for your credit risk project:

Credit Risk Prediction System

End-to-end credit default prediction platform with production-grade model serving and real-time inference API.

Impact

Achieved 11% performance improvement (ROC-AUC: 0.71 → 0.79) through strategic feature engineering on payment behavior datasets.

Technical Approach
Feature Engineering: Designed 30/60/90-day rolling window aggregations to capture temporal patterns in transaction behavior—transforming raw payment variables into signals that encode financial risk dynamics
Model Development: Built and validated a predictive system that bridges the domain knowledge gap between raw transaction data and credit risk patterns
Production Architecture: Implemented real-time inference API with serialized model serving, enabling low-latency credit decisions at scale
Interpretability: Applied SHAP and coefficient-based feature importance analysis to validate model decisions and align predictions with financial risk factors
Why This Matters

Most credit models treat transactions as static snapshots. This project demonstrates that temporal aggregation patterns reveal default risk more effectively than point-in-time features—a principle essential for building trustworthy risk systems in fintech and lending platforms.

Skills Demonstrated

Applied ML · Feature Engineering · Production Model Serving · Financial Domain Knowledge · Model Interpretability

Tips for positioning:

Lead with the 11% improvement—hiring managers see this immediately
Emphasize the domain knowledge gap you solved (this is what separates junior from senior ML work)
Highlight the production aspects—most student projects stop at notebooks; yours went live
Frame temporal windows as intentional design, not just preprocessing (this shows thought leadership)

Would you like me to adjust the tone, add code examples, or create a version formatted for a specific platform (GitHub README, personal site, etc.)?
```


## Observation

- The baseline prompt produced a technically polished portfolio description, but the output relied heavily on assumptions. Without additional context, the model inferred several project details that were not provided in the prompt, such as production model serving, real-time inference API, and specific implementation details.
- The output also immediately optimized for impressive presentation rather than accurately understanding the project's actual scope. While the generated narrative sounded professional, it risked overstating the project and mixing confirmed work with assumed capabilities.
- The biggest weakness of this baseline was the lack of direction: the model did not know the intended audience, purpose, positioning, or which engineering aspects should be emphasized. As a result, it optimized for a generic "successful AI project" narrative instead of a precise representation of the actual work.
