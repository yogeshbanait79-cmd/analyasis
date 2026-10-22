
import pandas as pd

df = pd.read_csv("Dataset .csv")

# Online delivery ka percentage
delivery_counts = df["Has Online delivery"].value_counts()

print("Online Delivery Count:")
print(delivery_counts)

print("\nOnline Delivery Percentage:")
print((delivery_counts / len(df) * 100).round(2))

# Delivery ke saath aur bina average rating
avg_rating = df.groupby("Has Online delivery")["Aggregate rating"].mean()

print("\nAverage Rating:")
print(avg_rating.round(2))
