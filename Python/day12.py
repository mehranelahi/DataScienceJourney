import pandas as pd

data = {
    "product": ["Laptop", "Phone", "Chair", "Desk", "Phone"],
    "category": ["Tech","Tech","Furniture","Furniture","Tech"],
    "sales": [1000, 700, 300, 500, 800]
}

df = pd.DataFrame(data)

# print(df)

# print(df.groupby("category")["sales"].sum())

# print(df.groupby("category")["sales"].mean())

# 1
print(df.groupby("category")["sales"].sum())

# 2
print(df.groupby("category")["sales"].max())

# 3
print(df.groupby("category")["product"].count())


