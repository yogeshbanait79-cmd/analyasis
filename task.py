import pandas as pd

df = pd.read_csv("Dataset .csv")

cuisines = df["Cuisines"].dropna().str.split(",").explode().str.strip()

top3 = cuisines.value_counts().head(3)

print("Top 3 Cuisines:")
print(top3)

print("\nPercentage of Restaurants:")
print((top3 / len(df) * 100).round(2))