import pandas as pd

df = pd.read_csv("sales.csv")

print("===== SALES REPORT =====\n")
total_products = df['product'].count()
print(f"Total Products: {total_products}")
total_sales = df['sales'].sum()
print(f"Total Sales: {total_sales}")
average_sales = df['sales'].mean()
print(f"Average Sales: {average_sales}")
highest_sales = df['sales'].max()
print(f"Highest Sales: {highest_sales}")
lowest_sales = df['sales'].min()
print(f"Lowest Sales: {lowest_sales}\n")


#############################

top_product = df.groupby('product')['sales'].max().idxmax()
print(f"Top Product --> {top_product}")
lowest_product = df.groupby('product')['sales'].min().idxmin()
print(f"Lowest Product: \n{lowest_product} --> ")
