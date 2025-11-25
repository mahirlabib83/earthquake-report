import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------
# Multizone Model Parameters for Bangladesh
# -------------------------------------------
years = 50
trials = 20000
b = 1.0

zones = {
    "Dauki": {
        "rate_M4": 0.25,
        "Mmin": 4.0,
        "Mmax": 7.5
    },
    "Madhupur": {
        "rate_M4": 0.15,
        "Mmin": 4.0,
        "Mmax": 7.2
    },
    "Chittagong": {
        "rate_M4": 0.30,
        "Mmin": 4.0,
        "Mmax": 7.8
    },
    "Megathrust": {
        "rate_M4": 0.05,
        "Mmin": 5.0,
        "Mmax": 8.5
    }
}

# Gutenberg-Richter sampling function
def sample_mag(a, b, size, Mmax):
    U = np.random.random(size)
    mags = (a - np.log10(U)) / b
    return np.minimum(mags, Mmax)

# Precompute a-values for each zone
for z in zones:
    rate = zones[z]["rate_M4"]
    Mmin = zones[z]["Mmin"]
    a = np.log10(rate) + b * Mmin
    zones[z]["a"] = a

# -------------------------------------------
# Monte Carlo Simulation
# -------------------------------------------
max_magnitudes = []

for _ in range(trials):
    all_mags = []
    
    for z in zones:
        # Poisson number of events
        lam = zones[z]["rate_M4"] * years
        n_events = np.random.poisson(lam)
        
        if n_events > 0:
            mags = sample_mag(
                zones[z]["a"],
                b,
                n_events,
                zones[z]["Mmax"]
            )
            all_mags.extend(mags)
    
    if len(all_mags) == 0:
        max_magnitudes.append(0)
    else:
        max_magnitudes.append(max(all_mags))

max_magnitudes = np.array(max_magnitudes)

# -------------------------------------------
# Probability Exceedances
# -------------------------------------------
def P(M):
    return np.mean(max_magnitudes >= M)

print("=== Multizone Bangladesh 50-year Probabilities ===")
print(f"P(M ≥ 6.0) = {P(6.0)*100:.2f}%")
print(f"P(M ≥ 7.0) = {P(7.0)*100:.2f}%")
print(f"P(M ≥ 8.0) = {P(8.0)*100:.2f}%")

# Histogram
plt.hist(max_magnitudes, bins=40)
plt.xlabel("Max Mag in 50-year Window")
plt.ylabel("Freq")
plt.title("Bangladesh Multizone Quake Monte Carlo")
plt.show()
