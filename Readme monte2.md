# Monte Carlo π Estimation

## Overview
This Python script estimates the value of π using the Monte Carlo method. The Monte Carlo technique relies on random sampling to approximate mathematical values. By randomly placing points inside a square and checking how many land inside a circle inscribed within it, we can estimate the ratio between the areas—leading to an approximation of π.

## Methodology
1. Generate Random Points Create N random (x, y) points within a unit square.
2. Check Inside Circle Count points that satisfy the equation `x² + y² ≤ 1` (inside a unit circle).
3. Estimate π Compute π using the formula

   [
        π ≈ 4 × (Number of points inside the circle / Total number of points)
   ]

4. Visualize and Analyze
   - Run simulations with increasing N values to observe the accuracy.
   - Plot estimated π values against different N values.

## Installation and Requirements
Ensure you have Python installed along with the following dependencies

```bash
pip install matplotlib numpy