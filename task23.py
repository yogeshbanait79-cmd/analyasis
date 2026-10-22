
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset .csv")

# Missing coordinates remove karo
df = df.dropna(subset=["Longitude", "Latitude"])

# Restaurant locations ka map-style scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(
    df["Longitude"],
    df["Latitude"],
    alpha=0.3,
    s=10
)

plt.title("Restaurant Geographic Distribution")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.show()

print("Restaurants plotted:", len(df))
