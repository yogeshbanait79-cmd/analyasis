
import pandas as pd

df = pd.read_csv("Dataset .csv")

# Most common restaurant chains
chain_counts = df["Restaurant Name"].value_counts()

print("Top 10 Restaurant Chains:")
print(chain_counts.head(10))

# Average rating and popularity (votes)
chain_analysis = df.groupby("Restaurant Name").agg(
    Restaurant_Count=("Restaurant Name", "count"),
    Average_Rating=("Aggregate rating", "mean"),
    Total_Votes=("Votes", "sum")
)

# Restaurants appearing more than once
chains = chain_analysis[chain_analysis["Restaurant_Count"] > 1]

print("\nChain Analysis:")
print(chains.sort_values("Restaurant_Count", ascending=False).head(10).round(2))
