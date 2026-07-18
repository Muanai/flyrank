# FL-02 Prompting Fundamentals on Real Tasks v2

## Task Overview

### Original Task
Write a portfolio description for my credit risk feature engineering project.

### Objective
Create a recruiter-facing portfolio description that demonstrates production-oriented ML engineering skills rather than presenting the project as a simple machine learning experiment.

### Why This Task Was Selected
This task was selected because crafting a compelling portfolio description is notoriously difficult; it requires balancing deep technical details with high-level business impact. By using a real, personal project instead of a toy example, this exercise clearly demonstrates how systematic prompt engineering can transform a generic, "academic-sounding" project summary into a highly targeted, production-oriented narrative that appeals directly to senior recruiters and hiring managers.

# Prompt Iterations

## Version 0 — Naive Prompt

### Technique Applied
None

### Prompt
Write a portfolio description for my credit risk project.

### Output Summary
- **ChatGPT**: Immediately generated a long, professional-sounding draft. The model hallucinated and added many specific assumptions (such as using Numba, FastAPI, SHAP, RAG) most likely from our previous chat sessions, that might be relevant but also might not be relevant to the actual project.
- **Claude**: Chose an interactive approach by asking clarifying questions first (project focus, audience, data scope) before generating a well-structured portfolio template tailored for ML/Data Science roles, complete with placeholders (like `[dataset name]`).

### Observation
Without sufficient context, ChatGPT tends to hallucinate technical specifications to make the description look impressive, while Claude prefers to provide an empty template after requesting a bit of context. This prompt is very weak because it forces the models to guess the goal, audience, and content of our project.

## Version 1 — Role Assignment

### Technique Applied
Role assignment

### Prompt
Act as a senior technical recruiter reviewing an AI engineer portfolio.
Write a portfolio description for my credit risk project.

### Output Summary
- **ChatGPT**: Produced a targeted description focused on the business problem, engineering ownership, and technical highlights. The tone shifted from a generic description to one emphasizing "production-oriented practices." It even offered a piece of recruiter advice at the end (advising against putting unusually large optimization claims in the headline without defense).
- **Claude**: Continued its interactive approach by asking 4 specific, senior-level questions (maturity level, technical achievement, real-world impact, geographic context). After "reading" the answers, it generated a comprehensive template focused heavily on system design, scalability (latency, inference), and operational reliability, along with a "Recruiter's Perspective" on what signals a senior engineer.

### Observation
Applying a persona ("senior technical recruiter") drastically improved the output. The models stopped treating this as a simple writing task and started acting as gatekeepers evaluating a candidate. ChatGPT immediately adjusted its language to emphasize engineering impact over just model accuracy. Claude used the persona to ask much sharper, production-focused questions before generating an incredibly detailed template that aligns with what top tech companies look for in a full-stack ML engineer.

## Version 2 — Context and Motivation

### Technique Applied
Context and motivation

### Prompt
Act as a senior technical recruiter reviewing an AI engineer portfolio.
I am an Applied AI Engineer building projects around Risk Intelligence and Operational Analytics.
Write a portfolio description for my credit risk feature engineering project.
The purpose is to demonstrate production-oriented ML engineering skills, not only model performance.

### Output Summary
- **ChatGPT**: Adjusted the positioning to highlight the project as an "ML engineering system" rather than just a modeling project. It successfully framed feature engineering as the crucial foundation for downstream decision systems and emphasized computational efficiency and robust data pipelines over algorithmic selection. It also suggested separating this into two projects (one for engineering, one for modeling).
- **Claude**: Acknowledged the framing immediately ("You're positioning this as feature engineering done right..."). It maintained its interactive approach, asking recruiter-focused questions to shape the narrative before generating the portfolio content.

### Observation
By providing context about the user's role ("Applied AI Engineer") and the specific motivation ("demonstrate production-oriented ML engineering skills, not only model performance"), both models immediately recognized the goal. They shifted the focus from "building a credit risk model" to "building a robust, scalable feature engineering pipeline." This proves that explicitly stating the "why" helps the model align with the user's strategic goals.

## Version 3 — Few-Shot Examples

### Technique Applied
Few-shot examples

### Prompt
Example style:
Project: Telligence, A telecoms infrastructure detection tools
Problem: Manual mapping is costly, while standard models fail to detect thin cables and heavily occluded poles in chaotic street environments. Severe class imbalance (e.g., rare providers) and environmental noise rendered off-the-shelf detection models ineffective.
Solution: Optimized YOLOv8 training with 1248px resolution scaling to recover fine-grained features like fiber optic cables. Implemented a custom inference engine with EXIF extraction and geospatial mapping (BPS shapefiles) to link detections to specific sub-districts.
Result: Successfully resurrected failing minority classes (~0% → ~50%). Delivered a deployment-ready tool that automates the conversion of raw street photos into mapped competitive intelligence. 0.763 mAP50 +24% accuracy from 0.52 baseline
Now create a similar description. *(Note: Adapted slightly for each model, maintaining the core few-shot example)*

### Output Summary
- **ChatGPT**: Strictly followed the requested format (Project, Problem, Solution, Result). It generated a highly focused and concise description emphasizing the reduction of feature generation latency and explicitly advised avoiding leading with model AUC to highlight the infrastructure engineering aspect.
- **Claude**: Adopted the requested format but added its own massive recruiter-oriented expansion. It provided a side-by-side comparison of "Generic Approach" vs "Recruiter-Oriented Framing", and generated a highly detailed portfolio description highlighting temporal correctness, leakage prevention, and systematic feature validation.

### Observation
Providing a few-shot example (Project, Problem, Solution, Result) gave the models a strict structural template to follow. ChatGPT produced a very concise and direct output that perfectly matched the example's length and tone. Claude used the example as a foundation to build a much more comprehensive, production-grade portfolio draft, adding defensive reasoning for every engineering choice. The few-shot technique effectively removed ambiguity about the desired output structure.

## Version 4 — Output Structure

### Technique Applied
Output structure

### Prompt
Act as a senior technical recruiter reviewing an AI engineer portfolio. I am an Applied AI Engineer building projects around Risk Intelligence and Operational Analytics. Write a portfolio description for my credit risk feature engineering project. The purpose is to demonstrate production-oriented ML engineering skills, not only model performance.

Example style: Project: Telligence... *(omitted for brevity)*

Return the answer using this structure:
- Problem
- Technical Approach
- Engineering Decisions
- Results
- Business Impact

### Output Summary
- **ChatGPT**: Strictly followed the requested markdown headers. The content was highly structured and professional, mapping the project details perfectly into Problem, Technical Approach, Engineering Decisions, Results, and Business Impact.
- **Claude**: Again took it a step further. It asked clarifying questions first, then generated the portfolio using the requested structure. However, it also provided a meta-analysis ("What I Changed from the Generic Version") explaining *why* it mapped the information that way, how recruiters read each sentence, and even suggested GitHub artifacts and interview talking points to back up the claims.

### Observation
Enforcing an output structure ensures that the models cover all necessary aspects of a portfolio (Problem to Business Impact) without rambling. ChatGPT treated it as a rigid template, while Claude used the structure as a framework but still added immense value by coaching the user on how to present and defend the project in an actual interview setting.

## Version 5 — Step Decomposition

### Technique Applied
Step decomposition

### Prompt
Act as a senior technical recruiter reviewing an AI engineer portfolio. I am an Applied AI Engineer building projects around Risk Intelligence and Operational Analytics. Write a portfolio description for my credit risk feature engineering project. The purpose is to demonstrate production-oriented ML engineering skills, not only model performance.

Example style: Project: Telligence... *(omitted for brevity)*

Return the answer using this structure:
- Problem
- Technical Approach
- Engineering Decisions
- Results
- Business Impact

Before writing:
1. Identify the target audience.
2. Extract the most important engineering contributions.
3. Determine measurable outcomes.
4. Draft the final portfolio description.

Only provide the final description.

### Output Summary
- **ChatGPT**: Strictly followed all instructions. It performed the required thinking steps internally (since it was asked to "Only provide the final description") and produced a highly cohesive, structured description highlighting the reduction of runtime from 58 seconds to milliseconds, framed perfectly for a recruiter.
- **Claude**: Despite the instruction to "Only provide the final description," Claude still output its "internal monologue" (Q&A style target audience identification, extraction of engineering wins) and added a meta-analysis on why it wrote the way it did for risk engineer/ML platform roles, before finally providing the meticulously crafted portfolio description.

### Observation
Step decomposition forced the models to evaluate the target audience and key engineering metrics *before* generating the content, leading to a much sharper final output. However, ChatGPT was much better at following the negative constraint ("Only provide the final description"), while Claude's alignment leans so heavily towards being helpful and transparent that it couldn't resist showing its work and providing additional coaching.

# Cross-Model Comparison

## ChatGPT

Strengths:
- **Obedience to Constraints**: ChatGPT is excellent at following explicit instructions, especially negative constraints (e.g., "Only provide the final description").
- **Structural Discipline**: It strictly adheres to requested formats, lengths, and markdown headers without unnecessary rambling.
- **Directness**: It treats the task as a direct generation exercise, providing clean, cohesive drafts ready for immediate use.

Weaknesses:
- **Hallucination in a Vacuum**: Without sufficient context (as seen in the Naive Prompt), it tends to invent technical details (like specific frameworks or metrics) to make the text sound professional.
- **Lack of Strategic Coaching**: It rarely volunteers advice on *why* certain phrasing works or how to present the work in an interview, acting more like a copywriter than a mentor.

## Claude

Strengths:
- **Highly Interactive & Mentoring**: Claude naturally adopts a coaching persona, asking sharp, senior-level clarifying questions before generating content.
- **Strategic Depth**: It frequently provides meta-analyses (e.g., "The Recruiter's Framing"), explaining the reasoning behind its choices and offering advice on supporting artifacts (GitHub repos, interview talking points).
- **Domain Nuance**: It generated incredibly rich, production-focused templates that deeply resonated with the specific demands of ML/Data Science roles.

Weaknesses:
- **Constraint Defiance (Helpfulness Override)**: Claude struggles with negative constraints (like "Only provide the final description") because its alignment leans so heavily towards transparency; it often outputs its internal "monologue" regardless.
- **Verbosity**: Its outputs can be extremely long, requiring the user to sift through extensive advice to extract the actual desired text.

## Key Difference
ChatGPT acts like a highly competent, obedient copywriter that strictly follows structural constraints and delivers exactly what is asked. Claude, conversely, acts like a senior mentor who insists on coaching and explaining the strategic rationale behind the text, even when explicitly told not to. ChatGPT is better for zero-friction final drafts, while Claude is superior for brainstorming and understanding the "why" behind the output.

# Reusable Prompt Template

```text
Act as a [Role/Persona, e.g., Senior Technical Recruiter].

Your task is to help create [Artifact, e.g., a portfolio description].

Context:
I am a [Your Title/Background] building projects around [Core Domain]. 
The purpose of this artifact is to demonstrate [Specific Goal, e.g., production-oriented ML engineering skills, not just model performance].

Example style:
[Provide a brief, high-quality example of the desired tone and structure]

Before writing:
1. Identify the target audience and their core concerns.
2. Extract the most important technical or engineering contributions.
3. Determine measurable, quantitative outcomes.
4. Draft the final content based on the above steps.

Return the output using this structure:
## [Section 1]
## [Section 2]
## [Section 3]

Constraints:
- Do not include conversational filler or internal thinking steps in the final output.
- Only provide the final [Artifact].
```