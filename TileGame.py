from node import *
import sys
from queue import PriorityQueue

def main():
    if len(sys.argv) >=2 :
        filename = sys.argv[1]
        with open(filename) as f:
            lines = [line.rstrip() for line in f]
        for i in range(0, len(lines), 2):
            start = lines[i].split(" ")
            goal = lines[i+1].split(" ")
            n = Node(start, None, "Start", True)
            if n.solvable(goal):
                print()
                print("Breadth-first algorithm")
                numberExplored, explored, fringe = search(n, goal, 1)
                print("The number of broad explored: " + str(len(numberExplored)))
                print("The number of broad stored in memory: " + str(len(explored)))
                print("The number of the nodes on the fringe: " + str(len(fringe)))
                if len(sys.argv) == 3 and sys.argv[2] == "-v":
                    print("Verbose mode")
                    for i in numberExplored:
                        print(i)

                print()
                print("Depth-limited search algorithm")
                numberExplored_dls, explored_dls, fringe_dls = search(n, goal, 2)
                print("The number of broad explored: " + str(len(numberExplored_dls)))
                print("The number of broad stored in memory: " + str(len(explored_dls)))
                print("The number of the nodes on the fringe: " + str(len(fringe_dls)))
                if len(sys.argv) == 3 and sys.argv[2] == "-v":
                    print("Verbose mode")
                    for i in numberExplored:
                        print(i)
                print()
                print("A* - Manhattan Distance")
                numberExplored_a, explored_a, queue = informedSearch(n, goal)
                print("The number of broad explored: " + str(len(numberExplored_a)))
                print("The number of broad stored in memory: " + str(len(explored_a)))
                print("The number of the nodes on the fringe: " + str(queue.qsize()))
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

    numberExplored = []
    cost = 0

    while fringe:

        # BFS
        if searchType == 1:
            node = fringe.pop(0)
        elif searchType == 2:
            node = fringe.pop()
        #calculate the cost for each node
        cost += node.calcCost()
        #increment the number of node explore
        numberExplored.append(node.state)
        if node.isGoal(goal):
            rebuildSolution(node)
            return numberExplored, explored, fringe
        else:
            kids, moves = node.findKids()
            for i in range(len(kids)):
                if(kids[i] not in explored and node.getDepth() <= 10):
                    newNode = Node(kids[i], node, moves[i], False)
                    fringe.append(newNode)
                    explored.append(kids[i])
    return numberExplored, explored, fringe

def informedSearch (start, goal):
    """

    :param start:
    :param goal:
    :return:
    """
    explored = []
    queue = PriorityQueue()
    explored.append(start.state)
    queue.put((0,start))
    numberExplored = []
    while queue:
        node = queue.get()[1]
        numberExplored.append(node.state)
        if node.isGoal(goal):
            rebuildSolution(node)
            return numberExplored, explored, queue
        else:
            kids, moves = node.findKids()
            for i in range(len(kids)):
                if (kids[i] not in explored):
                    newNode = Node(kids[i], node, moves[i], False)
                    cost = newNode.diffTiles(goal) + newNode.calcCost()
                    explored.append(kids[i])
                    queue.put((cost, newNode))
    return numberExplored, explored, queue

def rebuildSolution(node):
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







