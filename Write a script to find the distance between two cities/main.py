from geopy.distance import great_circle

try:
    coordinates1 = tuple(map(float, input("Enter the coordinates of the first city seperated by a comma: ").split(',')))
    coordinates2 = tuple(map(float, input("Enter the coordinates of the second city seperated by a comma: ").split(',')))

    if len(coordinates1) != 2 or len(coordinates2) != 2:
        raise ValueError
except ValueError:
    print("Invalid input. Please enter the coordinates as a float.")
    exit()

print('Distance: {:.2f} km'.format(great_circle(coordinates1, coordinates2).kilometers))
