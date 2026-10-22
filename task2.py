
import pandas as pd

df = pd.read_csv("Dataset .csv")

# 1. Sabse zyada restaurants wali city
city_counts = df["City"].value_counts()

print("City with most restaurants:")
print(city_counts.head(1))

# 2. Har city ki average rating
city_ratings = df.groupby("City")["Aggregate rating"].mean()

print("\nAverage rating of each city:")
print(city_ratings.round(2))

# 3. Highest average rating wali city
print("\nCity with highest average rating:")
print(city_ratings.idxmax())
print("Average rating:", round(city_ratings.max(), 2))
