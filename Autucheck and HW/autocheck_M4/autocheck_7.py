points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}
copy_points = points.copy()



def calculate_distance(coordinates):
    total_distance = 0
      
    for index, coord in enumerate(coordinates[:-1]):
        x = coord
        y = coordinates[index + 1]
        
        a = (x, y) if x < y else (y, x)

        # if (a) in points:
        total_distance += copy_points.get(a, 0)
        # else:
        #     copy_points[a] = "Not distance" # for add new element in dict.


    return total_distance 


print(calculate_distance([0, 1, 3, 2, 0, 2, 6, 8]))
print(copy_points)

