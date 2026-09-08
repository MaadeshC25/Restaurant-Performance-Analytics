import pandas as pd
import random
import pyodbc

# 5 Hotels and 5 Regions
restaurants = [
    "Thalappakatti Biriyani", "Sangeetha Veg", "Anjappar Chettinad", 
    "Copper Chimney", "Buhari Hotel"
]

regions = ["North", "South", "East", "West", "Central"]
dishes = ["Biriyani", "Paneer Tikka", "Chicken 65", "Masala Dosa", "Pasta", "Fried Rice"]
delivery_partners = ["Swiggy", "Zomato", "Direct"]

data = []

# Data Generation Logic (5x5 = 25 Records)
for hotel in restaurants:
    for region in regions:
        
        revenue = random.randint(100000, 300000)
        expenses = random.randint(60000, 180000)
        profit = revenue - expenses
        profit_margin = round((profit / revenue) * 100, 2)

        
        famous_dish = random.choice(dishes)
        rating = round(random.uniform(3.8, 5.0), 1)
        customer_count = random.randint(500, 2000)
        top_partner = random.choice(delivery_partners)
        
        data.append([
            hotel, region, revenue, expenses, profit, 
            profit_margin, famous_dish, rating, customer_count, top_partner
        ])

# Create DataFrame
columns = [
    "Restaurant_Name", "Region", "Revenue", "Expenses", "Net_Profit", 
    "Profit_Margin_Pct", "Famous_Dish", "Rating", "Total_Customers", "Top_Delivery_Partner"
]

df = pd.DataFrame(data, columns=columns)

# Export to CSV
df.to_csv("Hotel_Performance_Analysis.csv", index=False)
print(f"CSV file created with {len(df)} records.")

# SQL Server 
try:
    conn = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=DESKTOP-2Q8S09B;"
        "DATABASE=Restaurants;"
        "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    print("Connected to SQL Server successfully!")

    # Insert Query
    placeholders = ",".join(["?"] * len(columns))
    sql_query = f"INSERT INTO Hotel_Analysis VALUES ({placeholders})"

    # Insert Data
    for row in df.values:
        cursor.execute(sql_query, tuple(row))
    
    conn.commit()
    print("Data inserted into SQL successfully!")

except Exception as e:
    print(f"Database Error: {e}")