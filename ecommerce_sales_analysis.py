import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

products =np.array(["Mobile", "Laptop", "Headphones", "Watch", "Tablet"])

price = np.array([20000, 50000, 2000, 3000, 10000])

quantity = np.array([15, 10, 25, 20, 12])

df = pd.DataFrame({
    "Products": products,
    "Price":price,
    "Quantity": quantity
})
print(df, "\n")

df["Discount"] = [10,15,85,8,12]

df["Final Price"] = df["Price"] - (df["Price"] * df["Discount"] / 100)

df["Revenue"] = df["Price"] * df["Quantity"]
print(df, "\n")

print("Total Revenue -> ", df["Revenue"].sum())
print("Average Product Price -> ", df["Price"].mean())
highest = df.loc[df["Revenue"].idxmax(), "Products"]
print("Highest Selling Product -> ", highest)


# Bar Chart-
plt.subplot(2,2,1)
plt.bar(df["Products"], df["Revenue"])
plt.title("Revenue by Product")
plt.xlabel("Products")
plt.ylabel("Revenue")

# Pie Chart-
plt.subplot(2,2,2)
plt.pie(
    df["Revenue"],
    labels=df["Products"],
    autopct="%1.1f%%"
)

plt.title("Revenue Distribution")

# Line Chart-
plt.subplot(2,2,3)
plt.plot(df["Products"], df["Quantity"], marker='o', color='r')
plt.title("Quantity Sold")
plt.xlabel("Products")
plt.ylabel("Quantity")
plt.grid(True)

# Scatter Chart-
plt.subplot(2,2,4)
plt.scatter(df["Price"], df["Quantity"])
plt.title("Price vs Quantity")
plt.xlabel("Price")
plt.ylabel("Qunatity")
plt.grid(True)

plt.tight_layout()
plt.savefig("Ecommerce_Project.png")
plt.show()