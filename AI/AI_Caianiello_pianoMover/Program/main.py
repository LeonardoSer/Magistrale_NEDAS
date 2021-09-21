#!/usr/bin/env python3                                                                          
import GameModel as game
import Heuristic as heuristic

myMaze = game.maze(0.4)
sol_path = heuristic.astar_search(myMaze)

print("Lenght of solution path: ", len(sol_path))
print("_____________________________________________________")
print("\ninitial configuration\n")

myMaze.describe("verbose")
