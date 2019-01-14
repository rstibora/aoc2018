def first_star(input):
    def manhattan_distance(coord_from, coord_to):
        return abs(coord_to[0] - coord_from[0]) + abs(coord_to[1] - coord_from[1])

    def get_convex_hull(coords):
        min_x = min([coord[0] for coord in coords])
        max_x = max([coord[0] for coord in coords])
        min_y = min([coord[1] for coord in coords])
        max_y = max([coord[1] for coord in coords])
        return ((min_x, min_y), (max_x, max_y))

    def find_closest_coord(coord, all_coords):
        distances = [(manhattan_distance(coord, other_coord), other_coord) for other_coord in all_coords]
        shortest_distance = min(distances, key=lambda x: x[0])
        if len([distance for distance in distances if distance[0] == shortest_distance[0]]) == 1:
            return shortest_distance[1]
        else:
            return None

    def is_on_border(coord, convex_hull):
        return coord[0] == convex_hull[0][0] or coord[0] == convex_hull[1][0] or coord[1] == convex_hull[0][1] or coord[1] == convex_hull[1][1]

    coord_area = {}
    coords = [(int(input_line.split(',')[0]), int(input_line.split(',')[1])) for input_line in input]
    for coord in coords:
        coord_area[coord] = 0
    convex_hull = get_convex_hull(coords)
    for x in range(convex_hull[0][0], convex_hull[1][0] + 1):
        for y in range(convex_hull[0][1], convex_hull[1][1] + 1):
            closest = find_closest_coord((x, y), coords)
            if not closest:
                continue
            if is_on_border((x, y), convex_hull):
                coord_area[closest] = None
                continue
            elif coord_area[closest] is not None:
                coord_area[closest] += 1
    return max([area for area in coord_area.values() if area])

def second_star(input):
    pass
