import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("day11/datacleaning.csv")

# Clean data
df["Category"] = df["Category"].astype(str).str.strip().str.title()
df["Category"] = df["Category"].fillna("Unknown")

# Fill missing numeric values
df["Customer_Satisfaction"] = df["Customer_Satisfaction"].fillna(df["Customer_Satisfaction"].median())
df["Total_Amount"] = df["Total_Amount"].fillna(df["Total_Amount"].median())
df["Loyalty_Score"] = df["Loyalty_Score"].fillna(df["Loyalty_Score"].median())

# Create Satisfaction Groups
def satisfaction_level(score):
    if score <= 2:
        return "Low"
    elif score == 3:
        return "Medium"
    else:
        return "High"

df["Satisfaction_Level"] = df["Customer_Satisfaction"].apply(satisfaction_level)

# Analyze sales by satisfaction level and category
sales_category = df.groupby(
    ["Satisfaction_Level", "Category"]
)["Total_Amount"].mean().unstack()

print(sales_category)

# Plot results using Matplotlib
sales_category.plot(kind="bar", figsize=(8, 5))

plt.title("Average Sales by Satisfaction Level and Category")
plt.xlabel("Satisfaction Level")
plt.ylabel("Average Total Amount")
plt.legend(title="Category")
plt.tight_layout()
plt.show()

# Correlation between satisfaction and sales
correlation = df["Customer_Satisfaction"].corr(df["Total_Amount"])
print("Correlation:", round(correlation, 2))