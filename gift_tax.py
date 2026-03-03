value = int(input("Gift value: "))

if value < 5000:
    print("No tax")
else:
    tax = value * 0.08
    print(f"Tax: {tax}")