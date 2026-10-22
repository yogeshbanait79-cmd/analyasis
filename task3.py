
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset .csv")

# Price range ki counting
price_counts = df["Price range"].value_counts().sort_index()

# Percentage calculate karo
price_percentage = (price_counts / len(df)) * 100

print("Restaurant Count by Price Range:")
print(price_counts)

print("\nPercentage by Price Range:")
print(price_percentage.round(2))

# Bar chart
price_counts.plot(kind="bar")
plt.title("Price Range Distribution")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()
