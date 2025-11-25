Bangladesh Multizone Earthquake Monte Carlo Simulation

A Python-based Monte Carlo simulation to estimate 50-year maximum earthquake magnitudes and exceedance probabilities across multiple seismic zones in Bangladesh. This project uses the Gutenberg-Richter law and Poisson statistics to model earthquake occurrence.

Features:

Multizone modeling: Simulates earthquakes in four key zones—Dauki, Madhupur, Chittagong, and Megathrust.

Monte Carlo simulation: Runs 20,000 trials to capture statistical variability.

Gutenberg-Richter magnitude sampling: Accurately generates magnitudes from a truncated exponential distribution.

Probability exceedances: Computes the likelihood of earthquakes exceeding critical thresholds (e.g., M ≥ 6.0, 7.0, 8.0).

Visualization: Plots histogram of maximum magnitudes over a 50-year window.

Example Output
Multizone Bangladesh 50-year Probabilities
P(M ≥ 6.0) = 85.34%
P(M ≥ 7.0) = 42.17%
P(M ≥ 8.0) = 5.62%


Histogram shows frequency distribution of simulated maximum magnitudes.

How It Works:

Define zones with annual rates, minimum & maximum magnitudes.

Precompute Gutenberg-Richter a-values from zone-specific rates.

Monte Carlo simulation:

For each trial, sample Poisson-distributed number of earthquakes in each zone.

Sample earthquake magnitudes using the Gutenberg-Richter law.

Record the maximum magnitude in the 50-year period.

Compute exceedance probabilities as the fraction of trials above a magnitude threshold.

Visualize results with a histogram.

Requirements:

Python 3.8+

NumPy

Matplotlib

Install dependencies via pip:

pip install numpy matplotlib

Usage:
python bangladesh_quake_sim.py


Prints probability of exceeding key magnitudes.

Displays histogram of maximum magnitudes.

Notes:

Truncated Gutenberg-Richter sampling ensures magnitudes never exceed Mmax for each zone.

Adjustable parameters:

years: duration of simulation window

trials: number of Monte Carlo runs

zones: seismic zones, rates, and magnitude bounds



Gutenberg, B., & Richter, C. F. (1944). Frequency of earthquakes in California.

Poisson process modeling for earthquake occurrences.
