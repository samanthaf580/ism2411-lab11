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

print(customer["email"])

# Exercise 4

