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

### Notes
What Changed in the Prompt

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