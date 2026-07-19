# Version 5 — Constraints and Quality Criteria

## Layer Applied
Constraints and quality criteria

## Prompt

```text
Act as a senior technical recruiter reviewing an AI engineer portfolio.

I am an Applied AI Engineer building projects around Risk Intelligence and Operational Analytics.

Write a portfolio description for my credit risk feature engineering project.

The purpose is to demonstrate production-oriented ML engineering skills, not only model performance.

Example style:
Project: Telligence, A telecoms infrastructure detection tools

Problem:
Manual mapping is costly, while standard models fail to detect thin cables and heavily occluded poles in chaotic street environments.

Solution:
Optimized YOLOv8 training with 1248px resolution scaling to recover fine-grained features like fiber optic cables. Implemented a custom inference engine with EXIF extraction and geospatial mapping to link detections to specific locations.

Result:
Successfully improved minority class detection and delivered a deployment-ready tool that automates competitive intelligence extraction.

Before writing:

Identify the target audience.
Extract the most important engineering contributions.
Determine measurable outcomes.
Draft the final portfolio description.

Constraints:

Only use information explicitly provided.
Do not invent production metrics, infrastructure scale, deployment claims, or business outcomes.
Focus on engineering decisions and trade-offs rather than only model performance.
Avoid generic AI buzzwords.
Keep the narrative suitable for senior ML engineers reviewing an AI engineering portfolio.

Return the answer using this structure:

Problem
Technical Approach
Engineering Decisions
Results
Business Impact

Only provide the final description.
```

## Output

```text
# Credit Default Prediction: Rolling Window Feature Engineering

## Problem

Static credit variables (income, employment, debt ratios) miss behavioral signals in payment history. A baseline model achieved ROC-AUC 0.71 using only static features. The gap suggested predictive value in transaction patterns, but extracting it efficiently posed a systems constraint: naive rolling window aggregation is O(N×M) per window, making brute-force approaches prohibitively slow.

The real problem wasn't statistical—it was computational. Good features that take 12 hours to compute aren't viable in production.

## Technical Approach

Built rolling window aggregations across three time horizons reflecting distinct financial risk regimes:
- 30-day windows: Recent payment stress
- 60-day windows: Payment consistency and regularity patterns
- 90-day windows: Long-term financial stability

Benchmarked three implementation approaches:
- Pure Python loops as the correctness baseline
- Pandas vectorization for optimized dataframe operations
- Numba JIT compilation for optimized numerical computation

Selected Numba because it provided significant computational improvements while maintaining readable Python-based implementation.

## Engineering Decisions

Focused on validating engineering trade-offs rather than selecting the fastest tool blindly.

Compared multiple approaches using the same feature computation logic to understand the trade-off between development simplicity, memory efficiency, and execution speed.

Validated the optimized implementation against the baseline approach to ensure performance improvements did not introduce calculation errors.

Designed temporal features around financial behavior patterns instead of generating arbitrary aggregations, prioritizing interpretability for risk analysis.

## Results

Improved model performance:
- Baseline static features: ROC-AUC 0.71
- Engineered behavioral features: ROC-AUC 0.79

Feature engineering improved predictive performance by capturing behavioral patterns that static variables could not represent.

The benchmark demonstrated that implementation choices significantly affect the feasibility of building richer behavioral features, with Numba providing the most suitable balance for this workload.

## Business Impact

Created a more reliable foundation for credit risk intelligence by transforming transaction history into interpretable behavioral signals.

The project demonstrates production-oriented ML engineering thinking: improving model capability requires not only better algorithms, but also efficient feature computation, validation discipline, and careful engineering trade-offs.
```

### Notes
What Changed in the Prompt

The prompt added explicit constraints and quality criteria. It instructed the model to avoid unsupported assumptions, focus on engineering decisions, and prioritize accuracy over making the project appear more impressive.

This was added because previous iterations produced strong narratives but frequently introduced details that were not part of the actual implementation, such as production-scale infrastructure, latency requirements, and deployment scenarios.

### What Improved in the Output

This was the most accurate output compared to previous versions.

The model maintained the stronger storytelling from earlier iterations while removing many unsupported claims. It focused on the actual engineering contribution: benchmarking Python loops, Pandas, and Numba to enable more complex behavioral feature engineering.

The output also better represented the original motivation of the project. Instead of presenting Numba only as an optimization trick, it connected the computational improvement with the ability to build richer temporal risk signals that would otherwise be impractical.

### What Still Failed

The output became slightly too conservative and removed some useful technical depth.

While avoiding hallucination, it simplified some engineering details that could demonstrate stronger systems thinking, such as the specific behavioral patterns discovered from payment history and the reasoning behind rolling window selection.

The business impact section was also less concrete because the model avoided making any claims beyond the available evidence.

### What I Would Try Next

Create a final reusable prompt that combines the strengths of previous iterations:

Keep the structured output from Version 4.
Keep the accuracy constraints from Version 5.
Provide enough project-specific context to generate a detailed but truthful portfolio case study.