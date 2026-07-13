engine_temperature = int(input("Engine temperature: "))
oil_pressure = float(input("Oil pressure: "))
if engine_temperature > 110 or oil_pressure < 20:
    print("WARNING!")
else:
    print("Engine OK")