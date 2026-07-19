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
Here is a portfolio description for your credit risk project:

**Credit Risk Prediction Project**

In this project, I developed a machine learning model to predict credit risk. I used historical financial data to train various algorithms, achieving high accuracy in classifying default versus non-default loans. The project involved data cleaning, feature engineering, model training, and evaluation. This demonstrates my ability to handle complex datasets and apply predictive modeling techniques to solve real-world financial problems.
```

## Notes

### What Changed in the Prompt
Nothing; this is the baseline prompt.

### What Improved in the Output
N/A

### What Still Failed
The output is generic and filled with assumptions. It reads like a generic AI template rather than a real project description. It invents details (like high accuracy, classifying default vs non-default, and the specific pipeline steps) that were never provided in the prompt.

### What I Would Try Next
Add a clear goal to focus the output away from a generic summary and toward a specific outcome for a technical audience.

---

# Version 1 — Clear Goal

## Layer Applied
Clear goal

## Prompt

```text
Write a portfolio description for my credit risk project.

The goal is to explain the project clearly for a technical audience.
```

## Output

```text
I'll create a technical portfolio description for your credit risk project.

Here's a technical portfolio description for your credit risk project:

Credit Risk Prediction System

Production-grade credit default prediction model with real-time inference serving and explainable feature importance validation.

Problem Statement

Standard credit scoring approaches treat payment transactions as static snapshots, missing temporal patterns that correlate with default risk. Raw transaction variables alone lack the domain structure needed for effective risk modeling—requiring engineered features that capture behavioral dynamics.

Technical Solution

Feature Engineering Pipeline

Computed rolling window aggregations (30, 60, 90-day windows) on transaction payment history to extract temporal patterns and behavioral signatures
Engineered features capturing payment frequency, amount velocity, and consistency patterns that raw variables obscure
Addressed the domain knowledge gap by embedding financial risk semantics into feature space through careful window selection and aggregation choices

Model Development & Validation

Trained baseline model achieving ROC-AUC 0.71 on raw features
Feature engineering iteration improved performance to ROC-AUC 0.79 (+11% absolute improvement)
Validated feature importance using SHAP values and model coefficients to confirm risk factor alignment
Ensured model decisions map to interpretable financial behavior patterns

Production Architecture

Implemented serialized model serving for low-latency inference
Built real-time inference API enabling synchronous credit decisions at scale
Designed system to support production deployment patterns (model versioning, feature caching, request logging)
Key Insights

The 11% performance lift came from recognizing that temporal aggregation window selection is domain-critical. Transaction patterns over different time horizons encode different aspects of credit risk (recent behavior vs. historical stability), requiring intentional engineering rather than brute-force feature selection.

Technical Skills

Applied machine learning · Feature engineering · Production ML systems · Model interpretability (SHAP) · Financial risk modeling · API design
```

## Notes

### What Changed in the Prompt
The prompt added a clear goal by specifying that the portfolio description should explain the project for a technical audience.

### What Improved in the Output
The output became more technically focused compared to the baseline. It shifted from a generic project showcase into a more engineering-oriented explanation by introducing sections such as Problem Statement, Feature Engineering Pipeline, Model Development & Validation, and Key Insights.

The model also placed more emphasis on the relationship between temporal features and credit risk, rather than only presenting the project as a high-performing prediction model.

### What Still Failed
The output still introduced unsupported assumptions about production capabilities, including real-time inference serving, model versioning, feature caching, and request logging. These details were not explicitly provided in the prompt and could misrepresent the actual project scope.

The description also still framed the project primarily as a "Credit Risk Prediction System" rather than focusing on the feature engineering infrastructure aspect.

### What I Would Try Next
Provide information about the intended audience and the actual engineering scope of the project to prevent the model from inventing production details and to make the narrative better aligned with the real implementation.

---

# Version 2 — Defined Audience

## Layer Applied
Defined audience

## Prompt

```text
Write a portfolio description for my credit risk project.

The goal is to explain the project clearly for a technical audience.

The audience is a senior machine learning engineer reviewing an AI engineer portfolio.
```

## Output

```text
I'll craft a technical portfolio description targeting senior ML engineers reviewing your work.

Here's a technical portfolio description crafted for senior ML engineer review:

Credit Default Prediction: From Feature Poverty to Production Risk Model

An end-to-end case study in bridging the domain knowledge gap that separates baseline models from interpretable, production-ready risk systems.

The Core Problem

Transaction payment data is feature-poor: raw variables (amount, date, status) lack the semantic structure to encode credit risk. A naive baseline model achieved ROC-AUC 0.71—not because of algorithmic insufficiency, but because the feature space itself was underconstrained by domain theory. The challenge was engineering a feature representation that captures the temporal and behavioral dynamics that lenders actually use to assess default risk.

Solution Architecture

Feature Engineering as Domain Modeling
The breakthrough came from recognizing that payment risk operates across multiple temporal scales:

30-day windows capture acute payment stress (immediate liquidity constraints)
60-day windows reveal consistency patterns (habitual vs. anomalous behavior)
90-day windows encode longer-term financial stability signals

Rather than blindly aggregating, I designed rolling window features to explicitly model these behavioral regimes. This isn't feature selection—it's embedding financial domain knowledge into feature space through careful temporal decomposition.

Results & Validation

Baseline (raw features): ROC-AUC 0.71
Post-engineering: ROC-AUC 0.79 (+11% absolute improvement, +15% relative lift)
Critical validation step: SHAP analysis confirmed that learned feature importance aligned with financial domain theory (payment consistency as top signal, not statistical artifact)
Coefficient-based interpretation ensured decision logic maps to explainable risk factors

Production Considerations

Implemented serialized model serving architecture for low-latency synchronous inference
Real-time API design supporting sub-100ms request latency
Feature pipeline designed for operational robustness (lookback window consistency, feature staleness handling, edge case management for sparse transaction histories)
What This Demonstrates

For senior engineers, the value is in the thinking:

Domain-driven feature engineering: You didn't just throw features at the model; you translated domain knowledge (temporal risk dynamics) into principled feature design
Separation of concerns: Clear distinction between what signals matter (domain question) vs. how to capture them (engineering question)
Validation rigor: SHAP/coefficient alignment proves the model isn't just fitting noise—it's learning genuine financial risk patterns
Production readiness: Beyond notebook validation; you designed for deployment constraints (latency, interpretability, operational reliability)
Epistemic humility: The 11% gain came from better framing, not architectural wizardry—a mature approach to ML
Technical Depth

Applied ML · Domain-driven feature engineering · Temporal pattern modeling · Production model serving · Explainable AI (SHAP) · Risk model validation
```

## Notes

### What Changed in the Prompt
The prompt added a specific target audience by defining the reader as a senior machine learning engineer reviewing an AI engineer portfolio.

### What Improved in the Output
The output became significantly more specialized. Instead of only describing what was built, the model started framing engineering decisions that would matter to an experienced ML reviewer, such as feature representation, temporal modeling, validation methodology, and separation between domain reasoning and implementation.

The language also shifted from a general portfolio style into a technical review style, emphasizing why certain engineering decisions were made rather than only listing technologies.

### What Still Failed
The output continued to assume production capabilities that were not explicitly confirmed, such as real-time API design, sub-100ms latency, serialized model serving, and feature staleness handling.

It also introduced some overly confident statements, such as claiming SHAP confirmed specific domain theories, even though the actual project analysis may not have measured those conclusions.

### What I Would Try Next
Add real project context, including the actual engineering scope, tools used, and the specific feature engineering approach, so the model can produce a technically accurate narrative instead of an idealized production system description.

---

# Version 3 — Real Context

## Layer Applied
Real context

## Prompt

```text
Write a portfolio description for my credit risk project.

The goal is to explain the project clearly for a technical audience.

The audience is a senior machine learning engineer reviewing an AI engineer portfolio.

Context:
This project focuses on credit risk feature engineering.
I benchmarked Python loops, Pandas, and Numba for rolling window feature generation.
The goal was to build behavioral features from transaction history that capture customer risk patterns beyond static variables.
```

## Output

```text
Now I'll update the project record and create a portfolio description tailored to your implementation focus:

Here's a portfolio description tailored for senior ML engineers, emphasizing your engineering rigor:

---

## Credit Default Prediction: Engineering Behavioral Features at Scale

**A systems-focused case study in balancing domain-driven feature design with computational efficiency—benchmarking implementation tradeoffs for temporal aggregation on transaction data.**

### The Problem

Static credit variables (income, employment history) miss the dynamic risk signals embedded in payment behavior. Building rich temporal features requires processing transaction sequences efficiently: a naive approach compounds domain complexity with computational complexity. The challenge was engineering a feature pipeline that captures behavioral patterns *and* scales.

### Solution: Implementation-Aware Feature Engineering

**The Core Engineering Problem**
Transaction histories generate massive feature matrices: for N customers with M transactions each, computing 30/60/90-day rolling window aggregations naively requires O(N×M) operations per window, per statistic. This isn't just a performance problem—it's a **systems design problem**.

**Benchmark-Driven Architecture**
I evaluated three implementation strategies for behavioral feature generation:

1. **Pure Python loops** (baseline)
   * Direct, interpretable transaction-by-transaction aggregation
   * Reveals domain logic clearly but unacceptably slow for production datasets
   * Useful as reference implementation for validation

2. **Pandas vectorization**
   * Leverages groupby + rolling for templatized lookback windows
   * 10-50× speedup depending on transaction sparsity
   * Pandas memory overhead becomes bottleneck at scale (millions of transactions)

3. **Numba JIT compilation** (selected approach)
   * Compiled loop kernels operating directly on numpy arrays
   * Maintains interpretability while achieving 100-200× speedup over pure Python
   * Minimal memory footprint; viable for production feature pipelines
```

## Notes

### What Changed in the Prompt
The prompt added real project context by explaining the actual focus of the project: benchmarking Python loops, Pandas, and Numba for rolling window feature generation to create behavioral credit risk features.

### What Improved in the Output
This was the largest improvement so far. The model stopped treating the project as a generic credit prediction system and reframed it as a feature engineering and systems optimization problem.

The output correctly identified the engineering contribution as the benchmark between different implementation strategies and connected the optimization work (Numba) with the practical challenge of building scalable behavioral features.

The narrative also became closer to the actual project intent: demonstrating software engineering and ML systems thinking rather than only presenting model performance.

### What Still Failed
The output still introduced several unsupported assumptions, including production-scale datasets, millions of transactions, specific complexity analysis, exact speed improvements (100-200×), and production deployment considerations.

Some technical explanations were also stronger than what was actually implemented. For example, it described Numba as a production feature pipeline solution, while the actual work was primarily a benchmarking experiment to evaluate computational trade-offs.

### What I Would Try Next
Add a required output format and stronger constraints to guide the model toward an accurate portfolio description while preventing unsupported production claims.

---

# Version 4 — Structured Format

## Layer Applied
Specified output format

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

Context:
This project focuses on credit risk feature engineering.
I benchmarked Python loops, Pandas, and Numba for rolling window feature generation.
The goal was to build behavioral features from transaction history that capture customer risk patterns beyond static variables.

Return the answer using this structure:

Problem
Technical Approach
Engineering Decisions
Results
Business Impact
```

## Output

```text
Here's your portfolio description using the structured format:

---

## Credit Default Prediction: Behavioral Feature Engineering

### Problem

Static credit variables—income, employment history, debt ratios—capture demographic risk but miss the dynamic behavioral signals embedded in transaction patterns. A baseline model using only static features achieved ROC-AUC 0.71, leaving 15-20% of predictive signal on the table. The core challenge: How do you efficiently extract temporal risk patterns from transaction history at scale?

This is fundamentally an engineering problem, not just a modeling one. Naive rolling window aggregation requires O(N×M) complexity per window per metric, quickly becoming prohibitive for production systems.

...

## Business Impact

Risk model deployment:
- Improved default prediction accuracy
- Better risk segmentation
- More explainable lending decisions
```

## Notes

### What Changed in the Prompt
The prompt introduced a strict output structure by defining five required sections: Problem, Technical Approach, Engineering Decisions, Results, and Business Impact.

Previously, the model had freedom to decide the narrative structure, which could result in inconsistent emphasis. This change forced the model to separate the technical implementation, engineering reasoning, measurable outcomes, and business relevance.

### What Improved in the Output
The output became significantly easier to evaluate from a technical hiring perspective.

Instead of only describing the project as a machine learning experiment, the model created a clearer engineering narrative. The "Engineering Decisions" section was especially valuable because it forced discussion around why Numba was selected, why temporal windows were designed, and how optimization decisions were validated.

The structure also improved the balance between technical depth and business impact. The project was no longer only about achieving better ROC-AUC, but about building a reliable feature engineering foundation for risk intelligence systems.

### What Still Failed
Although the structure improved the storytelling, the model still generated unsupported technical assumptions.

The output added several claims that were not part of the actual implementation, such as production-scale transaction volumes, real-time inference requirements, exact latency targets, and large organizational impact.

The structured format helped organize information, but it did not prevent the model from filling missing details with plausible-sounding engineering scenarios.

### What I Would Try Next
Add explicit constraints requiring the model to only use verified project information and avoid inventing deployment details, infrastructure scale, or business metrics that were not measured.

---

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

Context:
This project focuses on credit risk feature engineering.
I benchmarked Python loops, Pandas, and Numba for rolling window feature generation.
The goal was to build behavioral features from transaction history that capture customer risk patterns beyond static variables.

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

## Notes

### What Changed in the Prompt
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

---

## Final Reusable Prompt

```text
Act as a [Target Audience, e.g., Senior Technical Recruiter] reviewing a [Document Type, e.g., AI Engineer Portfolio].

I am a [Your Role] building projects around [Your Domain/Focus Area].

Write a [Desired Output, e.g., portfolio description] for my [Specific Project Name/Topic].

The purpose is to demonstrate [Primary Goal, e.g., production-oriented ML engineering skills], not only [What to avoid focusing on, e.g., model performance].

Context:
[Insert 3-5 bullet points explaining the actual facts of the project: what you did, the tools you used, the baseline, the challenge, etc.]

Example style:
[Provide 1-2 examples of the tone, structure, or content you expect]

Before writing:
1. Identify the target audience.
2. Extract the most important contributions.
3. Determine measurable outcomes based only on the provided context.
4. Draft the final response.

Constraints:
- Only use information explicitly provided in the Context block.
- Do not invent metrics, infrastructure scale, deployment claims, or business outcomes.
- Focus on [Specific Aspect you care about, e.g., engineering decisions and trade-offs].
- Avoid generic buzzwords.
- Keep the narrative suitable for the target audience.

Return the answer using this structure:
- [Section 1, e.g., Problem]
- [Section 2, e.g., Technical Approach]
- [Section 3, e.g., Engineering Decisions]
- [Section 4, e.g., Results]
- [Section 5, e.g., Business Impact]

Only provide the final result.
```
