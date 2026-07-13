power = int(input("Power (HP): "))
weight = int(input("Weight (kg): "))
ratio = power / weight
print("Power: ", power, "HP")
print("Weight: ", weight, "kg")
print(f"Ratio: {ratio:.2f} HP/kg")
if ratio >= 0.5:
    print("Classification: Race car")
elif ratio >= 0.35:
    print("Classification: Supercar")
elif ratio >= 0.2:
    print("Classification: Sportcar")
else:
    print("Classification: Normal car")