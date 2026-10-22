
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset .csv")

# Rating distribution
plt.hist(df["Aggregate rating"], bins=10, edgecolor="black")
plt.title("Restaurant Ratings Distribution")
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()

# Most common rating range
rating_counts = pd.cut(df["Aggregate rating"], bins=10).value_counts()
print("Most common rating range:")
print(rating_counts.idxmax())

# Average votes
print("\nAverage number of votes:")
print(round(df["Votes"].mean(), 2))
