# from datetime import date

# print(date.today())  # 2026-11-02


# STUDENTS = 57
# PRESENT = 25
# LEAVE = 12
# ABSUANCE = 20
# print(PRESENT)
# customer = "noor foods"
# customer.upper()
#

# code = "ord-0042"

# code = code.replace("-", "")
# code = code.upper()
# print(code)
"""
priorities = {"low", "medium", "urgent"}

print(len(priorities))
print("urgent" in priorities)
print("critical" in priorities)
print(sorted(priorities))
"""

"""
customers = ["Noor Foods", "Bilal Traders", "Noor Foods", "Karachi Crafts"]
unique_customers = set(customers)

print(len(customers))
print(len(unique_customers))
print(sorted(unique_customers))
"""
""""
print(type({}))

seen = set()
seen.add("A101")
seen.add("A101")
print(seen)
"""
"""
this_week = {"Noor Foods", "Bilal Traders", "Karachi Crafts"}
last_week = {"Noor Foods", "Zara Textiles"}

print(sorted(this_week & last_week))
print(sorted(this_week - last_week))
print(sorted(this_week | last_week))
"""
"""
cities = ["Karachi", "Lahore", "Karachi", "Multan", "Lahore"]
unique_cities = set(cities)
print(len(unique_cities))
print(sorted(unique_cities))
"""
"""
order_ids = ["A101", "A102", "A101", "A103", "A102"]

seen = set()

for order in order_ids:
    if order in seen:
        print(f"Duplicate: {order}")
    else:
        seen.add(order)
"""
"""
last_month = {"Noor Foods", "Bilal Traders", "Zara Textiles"}
this_month = {"Noor Foods", "Karachi Crafts"}

stopped_order = last_month - this_month
new_customers = this_month - last_month
stayed = last_month.intersection(this_month)
print("stopped ordering: ", sorted(stopped_order))
print("New customers :", sorted(new_customers))
"""
"""
for total in [4500, 12800]:
    print(total)

for status in ("planned", "in_progress", "done"):
    print(status)

for priority in sorted({"low", "urgent", "medium"}):
    print(priority)
"""
raw_orders = [
    {"customer": " noor foods ", "status": "Delivered", "paid": 1},
    {"customer": "BILAL TRADERS", "status": " pending ", "paid": 0},
    {"customer": "noor foods", "status": "PENDING", "paid": 0},
]

orders = []
for raw in raw_orders:
    orders.append(
        {
            "customer": raw["customer"].strip().title(),
            "status": raw["status"].strip().lower(),
            "paid": bool(raw["paid"]),
        }
    )

for order in orders:
    print(order)

customers = set()
for order in orders:
    customers.add(order["customer"])
print(sorted(customers))
