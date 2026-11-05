# Exercise 1

customer = {
    "name": "Samantha",
     "email": "samanthaf580@usf.edu",
     "tier": "Gold",
     "ytd_spend": 1000.0
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)


# Exercise 2

customer["phone"] = "7274521560"

print(customer)

customer["tier"] = "Platinum"

print(customer)

del customer["email"]

print(customer)

# Exercise 3

print(customer.get("email", "no email on file"))

# print(customer["email"])

# Exercise 4

for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(key)


# .items returns both the key and the value, but without it, python only returns the keys.

#Exercise 5

tier_discounts = {
    "bronze": 0,
    "silver": .05,
    "gold": .10,
    "platinum": .15     
}


tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)

purchase_price = 200
final_price = purchase_price * (1 - discount_rate)

print("Tier:", tier)
print("Discount Rate:", f"{discount_rate:.0%}")
print("Final Price:", f"${final_price:.2f}")

# Exercise 6

dict1 = {
    "name": "Samantha",
    "tier": "platinum"
}

dict2 = {
    "name": "Zaynah",
    "tier": "gold"
}

dict3 = {
    "name": "Mijah",
    "tier": "silver"
}


customers = [dict1, dict2, dict3]

for customer in customers:
    tier = customer["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(f"{customer['name']}: {tier} - Discount: ${discount_amount:.2f}")


# Exercise 7

catalog = {
    "widget A": {"price": 9.99, "stock": 150}, 
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left!")



# Exercise 8

transactions = [
    {"region": "south", "amount": 300},
    {"region": "north", "amount": 150},
    {"region": "south", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount


for region in sorted(sales_summary):
    print(f"{region}: {sales_summary[region]}")
