
import pandas as pd

df = pd.read_csv("Dataset .csv")

# Most common cuisine combinations
combinations = df["Cuisines"].dropna().value_counts().head(10)

print("Top 10 Cuisine Combinations:")
print(combinations)

# Average rating of each combination
ratings = df.groupby("Cuisines")["Aggregate rating"].mean()

print("\nTop 10 combinations by average rating:")
print(ratings.sort_values(ascending=False).head(10).round(2))
