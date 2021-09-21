#!/usr/bin/env python3
import ctypes
import copy
import psutil
from datetime import datetime
import os # used for the shell command 'clear'
import GameModel as game

def expand_horizon(horizon, index):
    moves = ["top", "bottom", "right", "left"]
    for i in range(len(horizon[index].obstacles)):
        for move in moves:
            new_state = copy.deepcopy(horizon[index])
            if(new_state.mv(new_state.obstacles[i], move)):
                new_state.father = id(horizon[index])
                horizon.append(new_state)
    return horizon 

def astar_search(initial_state):
    horizon = []
    view = []
    horizon.append(initial_state)
    start = datetime.now()
    g = 0
    stop = 0 
    while not(stop): 
        f = 10000
        index = 0
        for i in range(len(horizon)):
            if(horizon[i].f < f):
                index = i
                f = horizon[i].f
        
        #print some infos at run time
        os.system("clear")
        print("Execution...")
        horizon[index].describe("")
        process = psutil.Process(os.getpid())
        print("occupied bytes: ", process.memory_info().rss)  # in bytes 
        
        stop = horizon[index].check_end()
        if not(stop):
            horizon = expand_horizon(horizon, index)
            view.append(horizon[index])
            horizon.pop(index)

    # time taken for the execution
    print("executed in", (datetime.now()-start), "\n")
    
    # format solution path
    path = []
    node = horizon[index]
    while (node.father != 0):
        path.append(node)
        node = (ctypes.cast(node.father, ctypes.py_object).value)
    return path[::-1] 
