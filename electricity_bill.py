def calculate_bill(units, cost_per_unit):
    bill = units * cost_per_unit
    return bill


units = float(input("Enter units consumed: "))
cost_per_unit = float(input("Enter cost per unit: "))

total_bill = calculate_bill(units, cost_per_unit)

print("Your electricity bill is:", total_bill)
