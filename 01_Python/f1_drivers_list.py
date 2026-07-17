drivers = []
number = int(input("How many drivers? "))
for i in range(number):
    driver = input(f"Driver {i+1}: ")
    drivers.append(driver)
print("============F1 DRIVERS LIST============")
for index, driver in enumerate(drivers, start=1):
    print(f"{index}. {driver}")
print("Total number of drivers: ", len(drivers))    