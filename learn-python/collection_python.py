
raw_orders = [
    {"customer": " noor foods ", "status": "Delivered", "paid": 1},
    {"customer": "BILAL TRADERS", "status": " pending ", "paid": 0},
    {"customer": "noor foods", "status": "PENDING", "paid": 0},
]
order=[]

for order in raw_orders:
    order.append(
        {
        "customer": order["customer"].strip().title()
        "status": order["status"].strip().tittle()
        "paid": bool(order["paid"])
        }
    )
for order in raw_order:
    print(order)
