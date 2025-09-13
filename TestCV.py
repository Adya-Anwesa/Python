import numpy as np
import matplotlib.pyplot as plt

# Simulate a potential sweep from -0.5V to 0.5V
potential = np.linspace(-0.5, 0.5, 500)

# Simulate a simple CV response: Gaussian peaks for anodic and cathodic currents
anodic_peak = 50 * np.exp(-((potential - 0.2)/0.05)**2)
cathodic_peak = -40 * np.exp(-((potential + 0.1)/0.05)**2)
current = anodic_peak + cathodic_peak

# Plot the CV curve
plt.plot(potential, current, color='blue', linewidth=2)
plt.title("Test Cyclic Voltammetry Curve")
plt.xlabel("Potential (V)")
plt.ylabel("Current (µA)")
plt.grid(True)
plt.show()
