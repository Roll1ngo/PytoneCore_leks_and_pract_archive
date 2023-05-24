points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7,
          (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}


def calculate_distance(coordinates):
    total_distance = 0
    # c = 0
    # not_distance_coordinats = []
    for index, coord in enumerate(coordinates[:-1]):
        x = coord
        y = coordinates[index + 1]
        # x = i
        # try:
        #    y= coordinates[c+1]

        # except IndexError:
        #     continue
        # c += 1
        a = (x, y) if x < y else (y, x)
        

        total_distance += points.get(a, 0)

    return total_distance


print(calculate_distance([0, 1, 3, 2, 0, 2, 8, 9]))
