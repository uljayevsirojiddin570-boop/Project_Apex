brand = input("car brand: ")
model = input("car model: ")
engine_power = int(input("engine power: "))
print("Car Brand: ", brand)
print("Car Model: ", model)
print("Engine Power: ", engine_power)
if engine_power >= 1000:
    classification = "Hypercar"
elif engine_power >= 700:
    classification = "Hyper sedan"
elif engine_power >= 500:
    classification = "Supercar"
elif engine_power >= 300:
    classification = "Sports car"
else:
    classification = "Normal car"
print("Classification: ", classification)
print("Recommended Track: ", end="")
if classification == "Hypercar":
    print("Silverstone Track")
elif classification == "Hyper sedan":
    print("Nurburgring Track")
elif classification == "Supercar":
    print("Monza Track")
elif classification == "Sports car":
    print("Spa Track")
else:
    print("City Road")