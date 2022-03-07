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
                print("woohoo solvable!")
                #TODO implemented BFGS
                #TODO implemented DFS
                #TODO implemented A* search
            else:
                print("Unsolvable")
        return
    else:
        print("Invalid input file")
        return





