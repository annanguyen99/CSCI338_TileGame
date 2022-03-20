from node import *
import sys
from queue import PriorityQueue
import matplotlib.pyplot as plt

def main():
    if len(sys.argv) >=2 :
        verbose = False
        if len(sys.argv) == 3 and sys.argv[1] == "-v":
            verbose = True
            filename = sys.argv[2]
        else:
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
                printResult(numberExplored, explored, fringe, verbose)
                print()
                print("Depth-limited search algorithm")
                numberExplored_dls, explored_dls, fringe_dls = search(n, goal, 2)
                printResult(numberExplored_dls, explored_dls, fringe_dls, verbose)
                print()
                print("A* - Number of Tiles Out of Place")
                numberExplored_a, explored_a, queue = informedSearch(n, goal)
                printResult(numberExplored_a, explored_a, queue, verbose)
                plotBar(numberExplored, numberExplored_dls, numberExplored_a )

            else:
                print("Unsolvable")
        return
    else:
        print("Invalid input file")
        return

def search(start, goal, searchType):
    """
    Search method which implement BFS and DLS
    :param start: the start node (puzzle broad)
    :param goal: the goal node (puzzle broad)
    :param searchType: 1 - BFS; 2- DLS
    :return: number of node explored, all the node explored, all the fringe
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
        # DLS
        elif searchType == 2:
            node = fringe.pop()
        #calculate the cost for each node
        cost += node.calcCost()
        #increment the number of node explore
        numberExplored.append(node)
        if node.isGoal(goal):
            rebuildSolution(node)
            return numberExplored, explored, fringe
        else:
            if searchType == 1:
                kids, moves = node.findKids(1)
            elif searchType == 2:
                kids, moves = node.findKids(2)
            for i in range(len(kids)):
                if(kids[i] not in explored and node.getDepth() <= 10):
                    newNode = Node(kids[i], node, moves[i], False)
                    fringe.append(newNode)
                    explored.append(kids[i])
    return numberExplored, explored, fringe

def informedSearch (start, goal):
    """
    Search method that perform A* search
    :param start: the start node
    :param goal: the goal node
    :return: number of node explored, all the node explored, all the fringe
    """
    explored = []
    queue = PriorityQueue()
    explored.append(start.state)
    queue.put((0,start))
    numberExplored = []
    while queue:
        node = queue.get()[1]
        numberExplored.append(node)
        if node.isGoal(goal):
            rebuildSolution(node)
            return numberExplored, explored, queue
        else:
            kids, moves = node.findKids(1)
            for i in range(len(kids)):
                if (kids[i] not in explored  and node.getDepth() <= 10):
                    newNode = Node(kids[i], node, moves[i], False)
                    cost = newNode.diffTiles(goal) + newNode.calcCost()
                    explored.append(kids[i])
                    queue.put((cost, newNode))
    return numberExplored, explored, queue

def rebuildSolution(node):
    """
    Rebuild solution method
    :param node: the goal node
    :return: the path to the solution
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

def plotBar(bfs, dls, astar):
    """

    :param explored:
    :return:
    """
    list =[]
    list.append(len(bfs))
    list.append(len(dls))
    list.append(len(astar))
    searches=["BFS", "DLS", "A*-Manhattan"]
    x_pos = [i for i, _ in enumerate(searches)]
    plt.bar(x_pos, list, color='yellow')
    plt.xlabel("Search type")
    plt.ylabel("Number of explored nodes")
    plt.xticks(x_pos, searches)
    plt.show()

def printResult(numberExplored, explored, fringe, verbose):
    """
    Print out the result
    """
    print("The number of broad explored: " + str(len(numberExplored)))
    print("The number of broad stored in memory: " + str(len(explored)))
    if fringe.__class__ == PriorityQueue:
        print("The number of the nodes on the queue: " + str(fringe.qsize()))
    else:
        print("The number of the nodes on the fringe: " + str(len(fringe)))
    if verbose:
        print("Verbose mode")
        for i in numberExplored:
            print(i)
main()







