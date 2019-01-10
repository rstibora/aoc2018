class LinkedList:
    class Node:
        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev if prev else self
            self.next = next if next else self

        def __repr__(self):
            return "{0}".format(self.value)

    def __init__(self):
        self.number_of_nodes = 0
        self.current = None

    def __repr__(self):
        output = ""
        current = self.current.prev
        while current is not self.current:
            output += "{0} ".format(current)
            current = current.prev
        output += "({0})".format(self.current)
        current = self.current.next
        while current is not self.current:
            output += " {0}".format(current)
            current = current.next
        return output

    def get_current(self):
        return self.current

    def set_current(self, node):
        self.current = node

    def insert(self, value):
        """
        Insert a new node before current node.
        """
        if not self.current:
            self.current = self.Node(value)
        else:
            prev = self.current.prev
            next = self.current
            self.current = self.Node(value, prev, next)
            prev.next = self.current
            next.prev = self.current
        self.number_of_nodes += 1
        return self.get_current()

    def iterate(self, idx):
        while idx < 0:
            self.current = self.current.prev
            idx += 1
        while idx > 0:
            self.current = self.current.next
            idx -= 1
        return self.get_current()

    def remove(self):
        """
        Remove current node. Next node will be current's node previous.
        """

        if self.number_of_nodes == 1:
            del self.current
            self.current = None
        else:
            current = self.current
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            del current
        self.number_of_nodes -= 1

def first_star(input):
    num_of_players = int(input[0].split()[0])
    last_marble = int(input[0].split()[6])
    scores = num_of_players * [0]

    marbles = LinkedList()
    marbles.insert(0)
    marble = 1
    while marble <= last_marble:
        for player in range(num_of_players):
            if marble % 23 == 0:
                marbles.iterate(-7)
                scores[player] += marbles.get_current().value + marble
                marbles.remove()
                marbles.iterate(1)
            else:
                marbles.iterate(2)
                marbles.insert(marble)
            marble += 1
    return max(scores)

def second_star(input):
    pass