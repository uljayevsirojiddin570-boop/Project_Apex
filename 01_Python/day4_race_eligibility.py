horse_power = int(input("Horse power: "))
top_speed = int(input("Top speed: "))
if horse_power >= 600 and top_speed >= 300:
    print("High Performance Car")
else:
    print("Fine car")