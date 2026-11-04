# example 1
"""
customer = "noor foods"
customer.upper()
print(customer)

customer = customer.upper()
print(customer)
"""

# example 2
"""
pasengers = "1o8"
pasengers = pasengers.replace("o", "0")
print(pasengers)
"""
# Example 2: lists can change example 3
"""
prices = [850, 1200, 400]
prices.append(3100)
prices[0] = 900
print(prices)
"""
# example 3
"""
cart = ["rice", "oil"]
cart.append("sugar")
cart[1] = "ghee"
cart.remove("rice")
print(cart)
"""
"""
 example 4
prices = [850, 1200, 400]

for i in range(len(prices)):
    prices[i] = round(prices[i] * 1.1)

print(prices)

"""
##example 5
"""
stock = 120
before = id(stock)
stock += 30
print(id(stock) == before)

prices = [850, 1200]
before = id(prices)
prices.append(400)
print(id(prices) == before)
"""
###example 6

location = [24.86, 67.01]
print(location[0])
location[0] = 31.52
