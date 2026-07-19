# Version 3 — Real Context

## Layer Applied
Real context

## Prompt

```
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

...

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