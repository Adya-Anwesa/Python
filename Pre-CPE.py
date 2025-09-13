import pandas as pd
import matplotlib.pyplot as plt

# Step 3a: Load your data
data = pd.read_csv("Pre-CPE.csv")  # Make sure the file is in the same folder

# Step 3b: Extract columns
Potential= data["Pot"]
Current= data["Cur"]

# Step 3c: Plot the CV curve
plt.figure(figsize=(6,4))
plt.plot(Potential, Current, color='red', linewidth=2, label="Pre Electrolysis")
plt.legend(loc='upper left',
fontsize=12,   
 frameon=False 
)
plt.xlabel("Potential (V $\t{vs.}$ Fc$^{0/+}$)")
plt.ylabel("J (mA/cm$^2$)")

plt.tight_layout()  # Automatically adjusts spacing so nothing is cut off
# Step 3d: Save the plot as an image
plt.savefig("Pre-CPE.png")
