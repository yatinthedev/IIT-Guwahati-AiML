# --------------------------------------
# Analyzing Customer Orders - Report Version
# --------------------------------------

# 1. Sample customer data
customers = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]

orders = [
    ("Alice", "Laptop", 800, "Electronics"),
    ("Alice", "Mouse", 20, "Electronics"),
    ("Bob", "T-Shirt", 25, "Clothing"),
    ("Bob", "Shoes", 60, "Clothing"),
    ("Charlie", "Vacuum Cleaner", 120, "Home Essentials"),
    ("Charlie", "T-Shirt", 25, "Clothing"),
    ("David", "Smartphone", 600, "Electronics"),
    ("Eva", "Blender", 45, "Home Essentials"),
    ("Eva", "Shoes", 60, "Clothing"),
    ("Frank", "Laptop", 800, "Electronics"),
    ("Frank", "Microwave", 90, "Home Essentials")
]

# 2. Organize data
customer_orders = {}
for name, product, price, category in orders:
    customer_orders.setdefault(name, []).append((product, price, category))

product_category = {prod: cat for _, prod, _, cat in orders}
unique_categories = set(product_category.values())

# 3. Customer spending & classification
customer_spending = {}
customer_classification = {}
for customer, items in customer_orders.items():
    total = sum(price for _, price, _ in items)
    customer_spending[customer] = total
    if total > 100:
        customer_classification[customer] = "High-Value"
    elif 50 <= total <= 100:
        customer_classification[customer] = "Moderate"
    else:
        customer_classification[customer] = "Low-Value"

# 4. Category revenue
category_revenue = {}
for _, _, price, category in orders:
    category_revenue[category] = category_revenue.get(category, 0) + price

# 5. Insights
unique_products = {product for _, product, _, _ in orders}
electronics_customers = [cust for cust, items in customer_orders.items()
                          if any(cat == "Electronics" for _, _, cat in items)]
top_spenders = sorted(customer_spending.items(), key=lambda x: x[1], reverse=True)[:3]

customers_per_category = {}
for category in unique_categories:
    customers_per_category[category] = {cust for cust, items in customer_orders.items()
                                        if any(cat == category for _, _, cat in items)}

multi_category_customers = set.intersection(*customers_per_category.values())
common_elec_clothing = customers_per_category["Electronics"] & customers_per_category["Clothing"]

# 6. Generate report
report_lines = []
report_lines.append("E-COMMERCE CUSTOMER ORDER ANALYSIS REPORT")
report_lines.append("=" * 50 + "\n")

# Executive Summary
report_lines.append("1. Executive Summary")
report_lines.append("-" * 50)
report_lines.append(f"Total Customers: {len(customers)}")
report_lines.append(f"Total Unique Products: {len(unique_products)}")
report_lines.append(f"Product Categories: {', '.join(unique_categories)}")
report_lines.append(f"Total Revenue: ${sum(customer_spending.values())}\n")

# Customer Classification
report_lines.append("2. Customer Classification")
report_lines.append("-" * 50)
for cust, total in customer_spending.items():
    report_lines.append(f"{cust}: ${total} ({customer_classification[cust]})")
report_lines.append("")

# Category Revenue
report_lines.append("3. Category-wise Revenue")
report_lines.append("-" * 50)
for cat, revenue in category_revenue.items():
    report_lines.append(f"{cat}: ${revenue}")
report_lines.append("")

# Key Insights
report_lines.append("4. Key Business Insights")
report_lines.append("-" * 50)
report_lines.append(f"Top 3 Spenders: {top_spenders}")
report_lines.append(f"Customers who purchased Electronics: {electronics_customers}")
report_lines.append(f"Customers who bought from ALL categories: {multi_category_customers}")
report_lines.append(f"Customers who bought both Electronics and Clothing: {common_elec_clothing}")
report_lines.append(f"Unique Products Sold: {unique_products}\n")

# Save to file
with open("customer_order_analysis_report.txt", "w") as f:
    f.write("\n".join(report_lines))

print("✅ Report generated: customer_order_analysis_report.txt")
