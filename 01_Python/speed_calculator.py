distance = float(input("distance (in km): "))
time = float(input("time (in hours): "))
fuel = float(input("fuel consumed (L): "))
speed = distance / time
fuel_efficiency = distance / fuel
fuel_consumed = fuel / distance * 100
print("=================RESULT=================")
print("Average Speed:.2f", speed, "km/h")
print("Fuel Efficiency:.2f", fuel_efficiency, "km/L")
print("Fuel Consumed:.2f", fuel_consumed, "L/100km")