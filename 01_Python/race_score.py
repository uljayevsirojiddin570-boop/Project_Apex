def calculate_points(position):
    if position == 1:
        return 25
    elif position == 2:
        return 18
    elif position == 3:
        return 15
    else:
        return 0
position = int(input("Position: "))
points = calculate_points(position)
print("Points: ", points)