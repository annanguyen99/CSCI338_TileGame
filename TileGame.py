# import statistics

from node import *
import sys
from queue import PriorityQueue
# import matplotlib.pyplot as plt
# from statistics import mean

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
        # Array that store all the BFS number of explored nodes
        breadth_num = []
        # Array that store all the BFS number of memory nodes
        breadth_explored = []
        # Array that store all the BFS number of fringe nodes
        breadth_fringe = []

        # Array that store all the DLS number of explored nodes
        depth_num = []
        # Array that store all the DLS number of memory nodes
        depth_explored = []
        # Array that store all the DLS number of fringe nodes
        depth_fringe = []

        # Array that store all the DLS number of explored nodes
        astar_num = []
        # Array that store all the DLS number of memory nodes
        astar_explored = []
        # Array that store all the DLS number of fringe nodes
        astar_fringe = []

        for i in range(0, len(lines), 2):
            start = lines[i].split(" ")
            goal = lines[i+1].split(" ")
            n = Node(start, None, "Start", True)
            if n.solvable(goal):
                print()
                print("Breadth-first algorithm")
                numberExplored_bfs, explored_bfs, fringe_bfs = repeated_search(n, goal, 1)
                printResult(numberExplored_bfs, explored_bfs, fringe_bfs, verbose)
                print()
                print("Breadth-first algorithm without repeated")
                numberExplored, explored, fringe = search(n, goal, 1)
                printResult(numberExplored, explored, fringe, verbose)
                breadth_num.append(len(numberExplored))
                breadth_explored.append(len(explored))
                breadth_fringe.append(len(fringe))
                print()
                print("Depth-limited search algorithm without repeated")
                numberExplored_dls, explored_dls, fringe_dls = search(n, goal, 2)
                printResult(numberExplored_dls, explored_dls, fringe_dls, verbose)
                depth_num.append(len(numberExplored_dls))
                depth_explored.append(len(explored_dls))
                depth_fringe.append(len(fringe_dls))
                print()
                print("Depth-limited search algorithm")
                numberExplored_dls_1, explored_dls_1, fringe_dls_1 = repeated_search(n, goal, 2)
                printResult(numberExplored_dls_1, explored_dls_1, fringe_dls_1, verbose)
                print()
                print("A* - Number of Tiles Out of Place")
                numberExplored_a, explored_a, queue = informedSearch(n, goal)
                printResult(numberExplored_a, explored_a, queue, verbose)
                astar_num.append(len(numberExplored_a))
                astar_explored.append(len(explored_a))
                astar_fringe.append(queue.qsize())

            else:
                print("Unsolvable")
        # plotBar(breadth_num, depth_num, astar_num, "Number of explored states")
        # plotBar(breadth_explored, depth_explored, astar_explored, "Number of all the nodes in memory")
        # plotBar(breadth_fringe, depth_fringe, astar_fringe, "Number of nodes in the fringe")
        return
    else:
        print("Invalid input file")
        return

def search(start, goal, searchType):
    """
    Search method which implement BFS and DLS without repeated nodes
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
            if (node.getDepth() <= 10):
                if searchType == 1:
                    kids, moves = node.findKids(1)
                elif searchType == 2:
                    kids, moves = node.findKids(2)
                for i in range(len(kids)):
                    if(kids[i] not in explored):
                        newNode = Node(kids[i], node, moves[i], False)
                        fringe.append(newNode)
                        explored.append(kids[i])
    return numberExplored, explored, fringe

def repeated_search(start, goal, searchType):
    """
    Search method which implement BFS and DLS with repeated nodes
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
            if (node.getDepth() <= 10):
                if searchType == 1:
                    kids, moves = node.findKids(1)
                elif searchType == 2:
                    kids, moves = node.findKids(2)
                for i in range(len(kids)):
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

# def plotBar(bfs, dls, astar, title):
#     """
#
#     :param explored:
#     :return:
#     """
#     list =[]
#     error =[]
#     list.append(mean(bfs))
#     error.append(statistics.stdev(bfs))
#     list.append(mean(dls))
#     error.append(statistics.stdev(dls))
#     list.append(mean(astar))
#     error.append(statistics.stdev(astar))
#     searches=["BFS", "DLS", "A*"]
#     x_pos = [i for i, _ in enumerate(searches)]
#     plt.bar(x_pos, list, color='yellow')
#     plt.xlabel("Search type")
#     plt.ylabel(title)
#     plt.errorbar(x_pos, list, yerr=error, fmt="o", color="r")
#     plt.xticks(x_pos, searches)
#     plt.show()

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







