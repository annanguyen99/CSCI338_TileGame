# CSCI338_TileGame
The 8- tile puzzle consists of an area divided into a 3x3 grid. On each grid square is a tile, expect for one 
square which remains empty (blank). Thus, there are eight tiles in the 8-puzzle. A tile that is next to the 
blank square can be moved into the empty space, leaving its previous position empty in turn. Tiles are 
numbered, 1 thru 8 for the 8-puzzle, so that each tile can be uniquely identified. The aim of the puzzle is 
to achieve a given configuration of tiles from a given (different) configuration by sliding the individual tiles 
around the grid as described above.


## Step to run the code in terminal
~~~
git init 
git clone https://github.com/annanguyen99/CSCI338_TileGame 
git pull origin master
~~~
## TODO LIST
- [ ] Develop a way to store the state of the 8-tile puzzle.  This will be your state description.
- [X] Develop  a  node  data  structure.    In  the  node  you  will  store  the  current  state  of  the  8-tile  puzzle,  a 
reference to the parent node, the move that led to the current state (did the blank move Up, Right, 
Down,  Left),  and  the  depth.  For  one  of  the  searches,  you  will  need  to  store  the  evaluation  of  the 
heuristic and the cost. You should only have one node data structure.
- [X] Develop a set of rules for generating children (successor states). When developing your children, make 
sure that they are expanded in clockwise order (blank moves U, R, D, L) when those moves are 
allowed from the parent state regardless of the search strategy. 
- [ ] Implement the breadth-first algorithm to solve the 8-tile puzzle allowing repeated states.  To avoid 
problems  of  tractability,  set  the  maximum  depth  that  can  be  opened  by  your  search  to  10;  the  root 
starts at depth of zero. Your program will print-out the sequence of moves needed to solve the puzzle 
(go from start to finish).   It will print out how many nodes were expanded and how many nodes were 
left on the fringe, and the maximum nodes stored in memory.
- [ ] Implement  verbose  mode.  In  verbose  mode  list  all  the  nodes  that  were  expanded  in  the  order  they 
were expanded until the goal is found or until you hit the limit of your search depth. This is required 
and it will help you debug your other searches.
- [ ] Implement the breadth-first algorithm to solve the 8-tile puzzle avoiding repeated states. To avoid 
problems  of  tractability,  set  the  maximum  depth  that  can  be  opened  by  your  search  to  10.  Your 
program will print-out the sequence of moves needed to solve the puzzle (go from start to finish).   It 
will print out how many nodes were expanded and how many nodes were left on the fringe, and the 
maximum nodes stored in memory.
- [ ] Implement  depth-limited  search  algorithm  allowing  repeated  states  (maximum  depth  10)  by 
making a small modification to your breadth-first algorithm (remember how you should alter how you 
add  your  children,  so  you  expand  them  in  the  needed,  clockwise  order).  Your  program  will  print-out 
the  sequence  of  moves  needed  to  solve  the  puzzle  (go  from  start  to  finish).      It  will  print  out  how 
many  nodes  were  expanded  and  how  many  nodes  were  left  on  the  fringe,  and  the  maximum  nodes 
stored in memory.
- [ ] Implement  a  depth-limited  search  algorithm  avoiding  repeated  states  (maximum  depth  10).  Your 
program will print-out the sequence of moves needed to solve the puzzle (go from start to finish).   It 
will print out how many nodes were expanded and how many nodes were left on the fringe, and the 
maximum nodes stored in memory.
- [ ] Implement a simple A* search allowing repeated states. You will use the tiles out of position as 
your  heuristic,  and  the  depth  of  the  node  as  the  cost.  To  avoid  problems  of  tractability,  set  the 
maximum  depth  that  can  be  opened  by  your  search  to  10.  Your  algorithm  will  simply  pick  the  best 
node to expand, will expand it. Your program will print-out the sequence of moves needed to solve the 
puzzle  (go  from  start  to  finish).      It  will  print  out  how  many  nodes  were  expanded  and  how  many 
nodes were left on the fringe, and the maximum nodes stored in memory.
