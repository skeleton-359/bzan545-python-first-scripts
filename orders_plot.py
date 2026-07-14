# Importing necessary packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating dataset called orders
orders = pd.read_csv("data/orders.csv")

# Printing info for plot including the top rows and shape of df
print("First rows")
print(orders.head())

print("Rows and columns")
print(orders.shape)

# Creating scatterplot
sns.scatterplot(x="quantity", y="order_total", hue="category", data=orders)
plt.show()
