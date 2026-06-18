import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Micro", "Keyboard", "Mouse"],
    "Price": [50000, 60000, 20000, 50000, 20000, 70000],
    "Sales": [10, 20, 15, 25, 30, 35]
}

df = pd.DataFrame(data)

print(df)
print(df.isnull().sum())

df = df.drop_duplicates()

df["Price"] = df["Price"].astype(int)
df["Sales"] = df["Sales"].astype(int)

df["Revenue"] = df["Price"] * df["Sales"]

df["Performance"] = df["Revenue"].apply(
    lambda x: "High" if x > 1000000 else "Medium"
)

summary = df.groupby("Product").agg(
    Total_Revenue=("Revenue", "sum"),
    Avg_Price=("Price", "mean"),
    Total_Sales=("Sales", "sum")
).reset_index()

print(summary)

