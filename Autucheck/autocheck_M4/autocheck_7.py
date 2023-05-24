coordinates = [0,1,3.2,0]
points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}
def calculate_distance(coordinates):
    total_distance = 0
    build_coor = ()
    for i in coordinates:
        x= coordinates[i]
        y= coordinates[i+1]
        build_coor += (x,y)
     
    print(build_coor)
    return build_coor

print(calculate_distance([0,1,3,4,2,5,4,3,]))
       