
def infinitize(list):
    index = 0
    while True:
        yield list[index]
        index = (index + 1) % len(list)
