top_speed = float(input("Top speed (km/h): "))
print("=================RESULT=================")
print("Top speed", top_speed, "km/h")
if top_speed >= 400:
    print("Category: hypercar")
elif top_speed >= 300:
    print("Category: supercar")
elif top_speed >= 200:
    print("Category: sportcar")
else:
    print("Category: normal car")