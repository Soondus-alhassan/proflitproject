import pandas as pd
import random
from datetime import datetime, timedelta

# Generate dummy data for Customers Table
num_customers = 100
customer_ids = list(range(1, num_customers + 1))
names = [f"Customer_{i}" for i in customer_ids]
emails = [f"customer_{i}@example.com" for i in customer_ids]
signup_dates = [(datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d') for _ in range(num_customers)]
locations = ["City_" + str(random.randint(1, 10)) for _ in range(num_customers)]

customers = pd.DataFrame({
    "CustomerID": customer_ids,
    "Name": names,
    "Email": emails,
    "SignUpDate": signup_dates,
    "Location": locations
})

# Generate dummy data for Products Table
num_products = 50
product_ids = list(range(1, num_products + 1))
product_names = [f"Product_{i}" for i in product_ids]
categories = random.choices(["Electronics", "Clothing", "Home & Garden", "Books"], k=num_products)
prices = [random.randint(10, 500) for _ in range(num_products)]
stock = [random.randint(0, 100) for _ in range(num_products)]

products = pd.DataFrame({
    "ProductID": product_ids,
    "ProductName": product_names,
    "Category": categories,
    "Price": prices,
    "Stock": stock
})

# Generate dummy data for Orders Table
num_orders = 200
order_ids = list(range(1, num_orders + 1))
order_dates = [(datetime.now() - timedelta(days=random.randint(0, 60))).strftime('%Y-%m-%d') for _ in range(num_orders)]
shipping_status = random.choices(["Pending", "Shipped", "Delivered"], k=num_orders)

orders = pd.DataFrame({
    "OrderID": order_ids,
    "CustomerID": random.choices(customer_ids, k=num_orders),
    "Date": order_dates,
    "ShippingStatus": shipping_status
})

# Generate dummy data for OrderDetails Table
order_detail_ids = list(range(1, num_orders * 2 + 1))  # Assuming 2 products per order on average
quantities = [random.randint(1, 3) for _ in range(num_orders * 2)]
product_choices = random.choices(product_ids, k=num_orders * 2)
total_prices = [products.iloc[p-1]['Price'] * q for p, q in zip(product_choices, quantities)]

order_details = pd.DataFrame({
    "OrderDetailID": order_detail_ids,
    "OrderID": [i for i in order_ids for _ in range(2)],
    "ProductID": product_choices,
    "Quantity": quantities,
    "TotalPrice": total_prices
})

# Save dataframes to CSV files
customers.to_csv("customers.csv", index=False)
products.to_csv("products.csv", index=False)
orders.to_csv("orders.csv", index=False)
order_details.to_csv("order_details.csv", index=False)