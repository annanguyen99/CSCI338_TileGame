import copy

class Node:
    """
    Node class that will store the current state of the 8-tile puzzle
    The code inspired from Professor Heather code for CSCI AI class Fall 2021
    :author : Anna Nguyen & Ethan Youso
    """

    def __init__(self, state, parent, action, root):
        """
        Constructor
        :param state:
        :param parent:
        :param action:
        :param root:
        """
        self.state = state
        self.parent = parent
        self.action = action
        if (root):
            self.depth = 0
        else:
            self.depth = 1 + self.parent.getDepth()
        self.cost = self.calcCost()

    def __repr__(self):
        """Return the state in three rows"""
        row1 = f"{self.state[0]}  {self.state[1]}  {self.state[2]} "
        row2 = f"{self.state[3]}  {self.state[4]}  {self.state[5]} "
        row3 = f"{self.state[6]}  {self.state[7]}  {self.state[8]} "
        return f"{row1}\n{row2}\n{row3}"

    def calcCost(self):
        """cost of this move - cumulative from parent"""
        if(self.depth == 0):
            return 0
        else:
            if self.action == "U":
                return self.getParent().getCost()+1
            elif self.action == "R":
                return self.getParent().getCost()+1
            elif self.action == "D":
                return self.getParent().getCost()+1
            elif self.action == "L":
                return self.getParent().getCost()+1

    def getCost(self):
        """return cost of node"""
        return self.cost

    def getDepth(self):
        """return depth of node"""
        return self.depth

    def getState(self):
        """return state of node"""
        return self.state

    def getParent(self):
        """return parent of node"""
        return self.parent

    def getAction(self):
        """return action of node"""
        return self.action

    def findBlank(self):
        """locate the blank"""
        for i in range(len(self.state)):
            if self.state[i] == "0":
                return i
        return -1

    def isGoal(self, goal):
        """returns true if this state matches the goal"""
        for i in range(len(self.state)):
            if self.state[i] != goal[i]:
                return False
        return True

    def findKids(self):
        """this generates the kids based on where the blank is
        """
        pos = self.findBlank()
        kids = []  # keep track of all the kids you can make from this point
        moves = []  # keep track of how the blank slide to make the kid
        if pos == 0:
            moveR = copy.deepcopy(self.state)
            moveD = copy.deepcopy(self.state)
            kids.append(self.swap(moveR, pos, 1))
            kids.append(self.swap(moveD, pos, 3))
            moves.append('R')
            moves.append('D')
        elif pos == 1:
            moveR = copy.deepcopy(self.state)
            moveD = copy.deepcopy(self.state)
            moveL = copy.deepcopy(self.state)
            kids.append(self.swap(moveR, pos, 2))
            kids.append(self.swap(moveD, pos, 4))
            kids.append(self.swap(moveL, pos, 0))
            moves.append('R')
            moves.append('D')
            moves.append('L')
        elif pos == 2:
            moveD = copy.deepcopy(self.state)
            moveL = copy.deepcopy(self.state)
            kids.append(self.swap(moveD, pos, 5))
            kids.append(self.swap(moveL, pos, 1))
            moves.append('D')
            moves.append('L')
        elif pos == 3:
            moveU = copy.deepcopy(self.state)
            moveR = copy.deepcopy(self.state)
            moveD = copy.deepcopy(self.state)
            kids.append(self.swap(moveU, pos, 0))
            kids.append(self.swap(moveR, pos, 4))
            kids.append(self.swap(moveD, pos, 6))
            moves.append('U')
            moves.append('R')
            moves.append('D')

        elif pos == 4:
            moveU = copy.deepcopy(self.state)
            moveR = copy.deepcopy(self.state)
            moveD = copy.deepcopy(self.state)
            moveL = copy.deepcopy(self.state)
            kids.append(self.swap(moveU, pos, 1))
            kids.append(self.swap(moveR, pos, 5))
            kids.append(self.swap(moveD, pos, 7))
            kids.append(self.swap(moveL, pos, 3))
            moves.append('U')
            moves.append('R')
            moves.append('D')
            moves.append('L')
        elif pos == 5:
            moveU = copy.deepcopy(self.state)
            moveD = copy.deepcopy(self.state)
            moveL = copy.deepcopy(self.state)
            kids.append(self.swap(moveU, pos, 2))
            kids.append(self.swap(moveD, pos, 8))
            kids.append(self.swap(moveL, pos, 4))
            moves.append('U')
            moves.append('D')
            moves.append('L')
        elif pos == 6:
            moveU = copy.deepcopy(self.state)
            moveR = copy.deepcopy(self.state)
            kids.append(self.swap(moveU, pos, 3))
            kids.append(self.swap(moveR, pos, 7))
            moves.append('U')
            moves.append('R')
        elif pos == 7:
            moveU = copy.deepcopy(self.state)
            moveR = copy.deepcopy(self.state)
            moveL = copy.deepcopy(self.state)
            kids.append(self.swap(moveU, pos, 4))
            kids.append(self.swap(moveR, pos, 8))
            kids.append(self.swap(moveL, pos, 6))
            moves.append('U')
            moves.append('R')
            moves.append('L')
        elif pos == 8:
            moveU = copy.deepcopy(self.state)
            moveL = copy.deepcopy(self.state)
            kids.append(self.swap(moveU, pos, 5))
            kids.append(self.swap(moveL, pos, 7))
            moves.append('U')
            moves.append('L')
        return kids, moves

    def swap(self, board, pos1, pos2):
        """mimcs sliding a tile"""
        temp = board[pos1]
        board[pos1] = board[pos2]
        board[pos2] = temp
        return board

    # for heap to work
    def __comp__(self, other):
        """ like implementing Comparable"""
        if self.cost < other.cost:
            return -1
        elif self.cost > other.cost:
            return 1
        else:
            return 0

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    # to determine if solvable
    def solvable(self, goal):
        """Determines if the state is solvable"""
        inversionCount = 0
        for i in range(len(self.state)):
            if self.state[i] != "0":
                inversionCount += self.inversionCount(i, goal)
        # print(f"number of inversions: {inversionCount}")
        # odd number of inversions are not solvable
        return inversionCount % 2 == 0

    def returnRank(self, num, goal):
        """returns the position of the where num is in goal"""
        for i in range(len(goal)):
            if (num == goal[i]):
                return i
        return -1

    def inversionCount(self, pos, goal):
        """An inversion is when a tile precedes another tile with a lower rank"""
        count = 0
        curRank = self.returnRank(self.state[pos], goal)
        for i in range(pos + 1, len(self.state)):
            if self.state[i] != "0":
                if curRank > self.returnRank(self.state[i], goal):
                    count += 1
        # print(f"tile {self.state[pos]} number of inversions: {count}")
        return count

    def diffTiles(self, goal):
        """

        :param goal:
        :return:
        """
        count = 0
        for i in range(len(self.state)):
            if self.state[i] != goal[i]:
                count += 1
        return count

    def calDistance(self):
        """

        :return:
        """
        goalDistance = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        totalDistance = 0
        for i in range(len(self.state)):
            x2, y2 = goalDistance[int(self.state[i]) - 1]
            x1, y1 = goalDistance[i]
            x = abs(x2 - x1)
            y = abs(y2 - y1)
            distance = x + y
            totalDistance += distance
        return totalDistance

if __name__ == "__main__":
    print("Hello! Welcome to fast testing node class")
    line = "1 2 3 4 0 6 7 5 8"
    start = line.split(" ")
    n = Node(start, None, "Start", True)
    print("Find blank method")
    print(n.findBlank())


