CART_LEFT = "<"
CART_RIGHT = ">"
CART_UP = "^"
CART_DOWN = "v"
TRACK_HORIZONTAL = "-"
TRACK_VERTICAL = "|"
TRACK_TURN_FW = "/"
TRACK_TURN_BCK = "\\"
TRACK_CROSSING = "+"

class UnexpectedTrackError(Exception):
    pass

def first_star(input):
    def tick_cart(cart, track):
        def increment_memory(memory):
            return (memory + 1) % 3

        # TODO: check that only one branch gets executed.
        position = cart[0]
        orientation = cart[1][0]
        memory = cart[1][1]
        # TODO: get rid of next_position.
        next_position = None
        if orientation == CART_LEFT:
            next_position = (position[0] - 1, position[1])
            next_track = track[next_position] if next_position in track else None
            if next_track == TRACK_TURN_FW:
                orientation = CART_DOWN
            elif next_track == TRACK_TURN_BCK:
                orientation = CART_UP
            elif next_track == TRACK_CROSSING:
                if memory == 0:
                    orientation = CART_DOWN
                elif memory == 2:
                    orientation = CART_UP
                memory = increment_memory(memory)
            elif not next_track == TRACK_HORIZONTAL:
                raise UnexpectedTrackError()
        elif orientation == CART_DOWN:
            next_position = (position[0], position[1] + 1)
            next_track = track[next_position] if next_position in track else None
            if next_track == TRACK_TURN_FW:
                orientation = CART_LEFT
            elif next_track == TRACK_TURN_BCK:
                orientation = CART_RIGHT
            elif next_track == TRACK_CROSSING:
                if memory == 0:
                    orientation = CART_RIGHT
                elif memory == 2:
                    orientation = CART_LEFT
                memory = increment_memory(memory)
            elif not next_track == TRACK_VERTICAL:
                raise UnexpectedTrackError()
        elif orientation == CART_RIGHT:
            next_position = (position[0] + 1, position[1])
            next_track = track[next_position] if next_position in track else None
            if next_track == TRACK_TURN_FW:
                orientation = CART_UP
            elif next_track == TRACK_TURN_BCK:
                orientation = CART_DOWN
            elif next_track == TRACK_CROSSING:
                if memory == 0:
                    orientation = CART_UP
                elif memory == 2:
                    orientation = CART_DOWN
                memory = increment_memory(memory)
            elif not next_track == TRACK_HORIZONTAL:
                raise UnexpectedTrackError()
        else:
            next_position = (position[0], position[1] - 1)
            next_track = track[next_position] if next_position in track else None
            if next_track == TRACK_TURN_FW:
                orientation = CART_RIGHT
            elif next_track == TRACK_TURN_BCK:
                orientation = CART_LEFT
            elif next_track == TRACK_CROSSING:
                if memory == 0:
                    orientation = CART_LEFT
                elif memory == 2:
                    orientation = CART_RIGHT
                memory = increment_memory(memory)
            elif not next_track == TRACK_VERTICAL:
                raise UnexpectedTrackError()
        return (next_position, orientation, memory)

    track, carts = parse_data(input)
    crashed = False
    while not crashed:
        moved_carts = {}
        sorted_carts = list(carts.items())
        sorted_carts.sort(key=lambda x: x[0][1])
        sorted_carts.sort(key=lambda x: x[0][0])
        for cart in sorted_carts:
            moved_cart = tick_cart(cart, track)
            if moved_cart[0] in moved_carts:
                moved_carts[moved_cart[0]] = ("x", moved_cart[2])
            else:
                moved_carts[moved_cart[0]] = (moved_cart[1], moved_cart[2])
        carts = moved_carts
        crashed = "x" in [value[0] for value in carts.values()]
    return [cart[0] for cart in carts.items() if cart [1][0] == "x"][0]

def second_star(input):
    pass

def parse_data(input):
    def parse_track(input):
        track = {}
        for line_no, line in enumerate(input):
            for char_no, char in enumerate(line):
                if char in ["-", "|", "+", "/", "\\", CART_LEFT, CART_RIGHT, CART_UP, CART_DOWN]:
                    track[(char_no, line_no)] = char
        return track

    def extract_carts_fix_track(track):
        carts = {}
        for pos, piece in track.items():
            if piece in [CART_DOWN, CART_UP]:
                track[pos] = "|"
                carts[pos] = (piece, 0)
            elif piece in [CART_LEFT, CART_RIGHT]:
                track[pos] = "-"
                carts[pos] = (piece, 0)
        return (track, carts)

    track = parse_track(input)
    return extract_carts_fix_track(track)