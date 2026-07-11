distance = float(input("distance (in km): "))
time = float(input("time (in hours): "))
fuel = float(input("fuel consumed (L): "))
speed = distance / time
fuel_efficiency = distance / fuel
fuel_consumed = fuel / distance * 100
print("=================RESULT=================")
print("Average Speed:", speed, "km/h")
print("Fuel Efficiency:", fuel_efficiency, "km/L")
print("Fuel Consumed:", fuel_consumed, "L/100km")