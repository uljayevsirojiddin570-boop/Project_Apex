horse_power = int(input("Horse power: "))
top_speed = int(input("Top speed: "))
weight = int(input("Weight: "))
if horse_power >= 600 and top_speed >= 300 and weight <= 1700:
    print("Race eligible")
else:
    print("Road car")