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

