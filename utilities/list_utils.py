class InfiniteList():
    def __init__(self, non_infinite_list):
        self.list = non_infinite_list

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.list):
            self.index = 0
        output = self.list[self.index]
        self.index += 1
        return output