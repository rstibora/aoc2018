import math

SEARCH_DISTANCE = 10000

def get_bbox(coords, inflate=0):
    min_x = min([coord[0] for coord in coords])
    max_x = max([coord[0] for coord in coords])
    min_y = min([coord[1] for coord in coords])
    max_y = max([coord[1] for coord in coords])
    return ((min_x - inflate, min_y - inflate), (max_x + inflate, max_y + inflate))

def get_ring_around_bbox(bbox, ring):
    ring_points = set([(x, bbox[0][1] - ring) for x in range(bbox[0][0] - ring, bbox[1][0] + ring + 1)])
    ring_points |= set([(x, bbox[1][1] + ring) for x in range(bbox[0][0] - ring, bbox[1][0] + ring + 1)])
    ring_points |= set([(bbox[0][0] - ring, y) for y in range(bbox[0][1] - ring, bbox[1][1] + ring + 1)])
    ring_points |= set([(bbox[1][0] - ring, y) for y in range(bbox[0][1] - ring, bbox[1][1] + ring + 1)])
    return ring_points

def manhattan_distance(coord_from, coord_to):
    return abs(coord_to[0] - coord_from[0]) + abs(coord_to[1] - coord_from[1])

def shift_coord(coord, shift):
    return ((coord[0] + shift[0], coord[1] + shift[1]))

def first_star(input):
    def find_closest_coord(coord, all_coords):
        distances = [(manhattan_distance(coord, other_coord), other_coord) for other_coord in all_coords]
        shortest_distance = min(distances, key=lambda x: x[0])
        if len([distance for distance in distances if distance[0] == shortest_distance[0]]) == 1:
            return shortest_distance[1]
        else:
            return None

    def is_on_border(coord, convex_hull):
        return coord[0] == convex_hull[0][0] or coord[0] == convex_hull[1][0] or coord[1] == convex_hull[0][1] or coord[1] == convex_hull[1][1]

    coords = [(int(input_line.split(',')[0]), int(input_line.split(',')[1])) for input_line in input]
    coords_area = {key:0 for key in coords}
    convex_hull = get_bbox(coords)
    for x in range(convex_hull[0][0], convex_hull[1][0] + 1):
        for y in range(convex_hull[0][1], convex_hull[1][1] + 1):
            closest = find_closest_coord((x, y), coords)
            if not closest:
                continue
            if is_on_border((x, y), convex_hull):
                coords_area[closest] = None
                continue
            elif coords_area[closest] is not None:
                coords_area[closest] += 1
    return max([area for area in coords_area.values() if area])

def second_star(input):
    def distance_to_all(coord, all_coords):
        return sum([manhattan_distance(coord, coord_to) for coord_to in all_coords])

    coords = [(int(input_line.split(',')[0]), int(input_line.split(',')[1])) for input_line in input]
    area_points = set()
    bbox = get_bbox(coords)
    for x in range(bbox[0][0], bbox[1][0]):
        for y in range(bbox[0][1], bbox[1][1]):
            if distance_to_all((x, y), coords) < SEARCH_DISTANCE:
                area_points.add((x, y))
    # Check in increasingly larger ring around the bounding box.
    new_points = True
    ring = 1
    while new_points:
        old_point_count = len(area_points)
        for point in get_ring_around_bbox(bbox, ring):
            if distance_to_all(point, coords) < SEARCH_DISTANCE:
                area_points.add(point)
        ring += 1
        new_points = len(area_points) != old_point_count
    # Find the biggest area.
    areas = []
    point_stash = set([area_points.pop()])
    while len(area_points):
        area = 0
        while len(point_stash):
            point = point_stash.pop()
            area += 1
            neighbours = [shift_coord(point, (-1, 0)), shift_coord(point, (1, 0)), shift_coord(point, (0, -1)), shift_coord(point, (0, 1))]
            for neighbour in neighbours:
                if neighbour in area_points:
                    area_points.remove(neighbour)
                    point_stash.add(neighbour)
        areas += [area]
    return max(areas)
