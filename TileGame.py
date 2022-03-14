from node import *
import sys

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        with open(filename) as f:
            lines = [line.rstrip() for line in f]
        for i in range(0, len(lines), 2):
            start = lines[i].split(" ")
            goal = lines[i+1].split(" ")
            n = Node(start, None, "Start", True)
            if n.solvable(goal):
                explore = []
                print("woohoo solvable!")
                print("BFS")
                explore.append(search(n, goal, 1))
                #TODO implemented DFS
                #TODO implemented A* search
            else:
                print("Unsolvable")
        return
    else:
        print("Invalid input file")
        return

def search(start, goal, searchType):
    """

    :param start: the start node (puzzle broad)
    :param goal: the goal node (puzzle broad)
    :param searchType: 1 - BFS
    :return:
    """
    explored = [] #states I have seen
    fringe = [] #stored kids
    fringe.append(start)
    explored.append(start.state)

    numberExplored = 0
    cost = 0

    while fringe:
        # BFS
        if searchType == 1:
            node = fringe.pop(0)
        #calculate the cost for each node
        cost += node.calcCost()
        #increment the number of node explore
        numberExplored += 1
        if node.isGoal(goal):
            rebuidSolution(node)
            return numberExplored
        else:
            kids, moves = node.findKids()
            for i in range(len(kids)):
                if(kids[i] not in explored and node.getDepth() <= 10):
                    newNode = Node(kids[i], node, moves[i], False)
                    fringe.append(newNode)
                    explored.append(kids[i])
    print("Unable to solve at the current depth")
    return numberExplored

def rebuidSolution(node):
    """

    :param node:
    :return:
    """
    stack = []
    while node != None:
        stack.append(node)
        node = node.getParent()
    solution = []
    while len(stack) > 0:
        s = stack.pop()
        solution.append(s.getAction())
    print(f"moves to solution: {solution}")

main()







