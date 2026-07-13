brand = input("car brand: ")
model = input("car model: ")
engine_power = int(input("engine power: "))
print("Car Brand: ", brand)
print("Car Model: ", model)
print("Engine Power: ", engine_power)
print("Classification: ", end="")
if engine_power > 700:
    print("Hypercar")
elif engine_power > 500:
    print("Supercar")
elif engine_power > 300:
    print("Sports Car")
else:
    print("Normal Car")