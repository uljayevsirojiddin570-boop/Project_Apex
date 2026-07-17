cars = []
number = int(input("How many cars? "))
for i in range(number):
    car = input(f"Enter car {i+1}: ")
    cars.append(car)
print("============YOUR GARAGE============")
for car in cars:
    print(car)
print("Total number of cars:", len(cars))