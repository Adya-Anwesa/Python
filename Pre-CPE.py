import pandas as pd
import matplotlib.pyplot as plt

# Step 3a: Load your data
data = pd.read_csv("Pre-CPE.csv")  # Make sure the file is in the same folder

# Step 3b: Extract columns
Potential= data["Pot"]
Current= data["Cur"]

# Step 3c: Plot the CV curve
plt.figure(figsize=(6,4))
plt.plot(Potential, Current, color='red', linewidth=2)
plt.title("Pre-CPE")
plt.xlabel("Potential (V)")
plt.ylabel("Current density (mA/cm2)")
plt.grid(True)

# Step 3d: Save the plot as an image
plt.savefig("Pre-CPE.png")

# Step 3e: Show the plot
plt.show()
