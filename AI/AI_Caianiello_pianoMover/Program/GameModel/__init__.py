#!/usr/bin/env python3
import random as rand

class maze:
    def __init__(self, density):
        
        self.father = 0
        self.board = [[0 for _ in range(10)] for _ in range(10)]
        self.board[9][0] = -1
        self.board[8][0] = -1
        self.board[9][1] = -1
        self.board[8][1] = -1
        
        self.density = density
        self.obstacles = []
        self.obstacles.append({"id": -1 , "coords":[[8,0], [8,1], [9,0], [9,1]]})
        self.fill_w_obstacles() 
        
        self.end_pos = {"id": "end_pos", "coords":[[0,8], [0,9], [1,8], [1,9]]}
        self.start_pos = {"id": "start_pos", "coords":[[8,0], [8,1], [9,0], [9,1]]}
        
        
        self.h = self.eval_state()
        self.g = 0
        self.f = self.h + self.g

    def fill_w_obstacles(self):
        obstacles_size =4
        i = 1 
        while( obstacles_size < self.density * 100):
            option = rand.randint(0, 2)
            
            if(option == 0):
                obstacles_size += self.put_Obstacles(i, 1)
                i += 1
            if(option == 1):
                obstacles_size += self.put_Obstacles(i, 2)
                i += 1
            if(option == 2):
                obstacles_size += self.put_Obstacles(i, 3)
                i += 1
 
    def put_Obstacles(self, i, dim):
        size = 0
        filling = True
        while(filling):
            x=rand.randint(0,9)
            y=rand.randint(0,9)
            if(self.board[x][y] == 0):
                self.board[x][y] = i 
                self.obstacles.append({"id": i, "coords":[[x,y]]})
                size += 1
                if(dim >= 2):
                    if(self.check_neighborhood(x, y)):
                        self.fill_2Neighborhood(i, x, y)
                        size += 1
                        if(dim == 3):
                            if(self.check_neighborhood(self.obstacles[i]["coords"][1][0], self.obstacles[i]["coords"][1][1])):
                                self.fill_2Neighborhood(i, self.obstacles[i]["coords"][1][0], self.obstacles[i]["coords"][1][1])                
                                size += 1
                filling = False
        return size

    def fill_2Neighborhood(self, i, x, y):
        filling = True
        while(filling):
            option = rand.randint(0,3)
            if(x-1 >= 0 and option==0 and self.board[x-1][y] == 0):
                self.board[x-1][y] = i
                self.obstacles[i]["coords"].append([x-1,y])
                filling = False
            if(x+1 <= 9 and option==1 and self.board[x+1][y] == 0):
                self.board[x+1][y] = i
                self.obstacles[i]["coords"].append([x+1,y])
                filling = False
            if(y-1 >= 0 and option==2 and self.board[x][y-1] == 0):
                self.board[x][y-1] = i
                self.obstacles[i]["coords"].append([x,y-1])
                filling = False
            if(y+1 <= 9 and option==3 and self.board[x][y+1] == 0):
                self.board[x][y+1] = i
                self.obstacles[i]["coords"].append([x,y+1])
                filling = False
    
    def check_neighborhood(self, x, y):
        if(x<9):
            if(self.board[x+1][y] == 0):
                return True
        if(x>0):
            if(self.board[x-1][y] == 0):
                return True
        if(y<9):
            if(self.board[x][y+1] == 0):
                return True
        if(y>0):
            if(self.board[x][y-1] == 0):
                return True
        return False

    def mv(self, obstacle, direction):
        ret_val = False
        
        if(direction == "right"):
            ret_val = self.mv_obst_r(obstacle)
        elif(direction == "left"):
            ret_val = self.mv_obst_l(obstacle)
        elif(direction == "top"):
            ret_val = self.mv_obst_top(obstacle)
        elif(direction == "bottom"):
            ret_val = self.mv_obst_btm(obstacle)
    
        if(ret_val and obstacle["id"]==-1):
            self.h = self.eval_state()
            self.g+=1
            self.f = self.h + self.g
        
        return ret_val

    def mv_obst_r(self, obstacle):
        move = True
        for i in range(len(obstacle["coords"])):
            coords = obstacle["coords"][i]
            if not (coords[1]+1 <= 9 and (self.board[coords[0]][coords[1]+1] == 0 or self.board[coords[0]][coords[1]+1] == obstacle["id"])):
                move = False
        if(move):
            for o in self.obstacles:
                if(o["id"] == obstacle["id"]):
                    for i in range(len(obstacle["coords"])):
                        coords = obstacle["coords"][i]
                        self.board[coords[0]][coords[1]] = 0
                    for i in range(len(obstacle["coords"])):
                        coords = obstacle["coords"][i]
                        self.board[coords[0]][coords[1]+1] = obstacle["id"] 
                        obstacle["coords"][i] = [coords[0], coords[1]+1] 
        return move

    def mv_obst_l(self, obstacle):
        move = True
        for i in range(len(obstacle["coords"])):
            coords = obstacle["coords"][i]
            if not (coords[1]-1 >= 0 and (self.board[coords[0]][coords[1]-1] == 0 or self.board[coords[0]][coords[1]-1] == obstacle["id"])):
                move = False
        if(move):
            for o in self.obstacles:
                if(o["id"] == obstacle["id"]):
                    for i in range(len(obstacle["coords"])):
                        coords = obstacle["coords"][i]
                        self.board[coords[0]][coords[1]] = 0
                    for i in range(len(obstacle["coords"])):
                        coords = obstacle["coords"][i]
                        self.board[coords[0]][coords[1]-1] = obstacle["id"] 
                        obstacle["coords"][i] = [coords[0], coords[1]-1] 
        return move
    
    def mv_obst_btm(self, obstacle):
        move = True
        for i in range(len(obstacle["coords"])):
            coords = obstacle["coords"][i]
            if not (coords[0]+1 <= 9 and (self.board[coords[0]+1][coords[1]] == 0 or self.board[coords[0]+1][coords[1]] == obstacle["id"])):
                move = False
        if(move):
            for o in self.obstacles:
                if(o["id"] == obstacle["id"]):
                    for i in range(len(obstacle["coords"])):
                        coords = obstacle["coords"][i]
                        self.board[coords[0]][coords[1]] = 0
                    for i in range(len(obstacle["coords"])):
                        coords = obstacle["coords"][i]
                        self.board[coords[0]+1][coords[1]] = obstacle["id"] 
                        obstacle["coords"][i] = [coords[0]+1, coords[1]]
        return move

    def mv_obst_top(self, obstacle):
        move = True
        for i in range(len(obstacle["coords"])):
            coords = obstacle["coords"][i]
            if not (coords[0]-1 >= 0 and (self.board[coords[0]-1][coords[1]] == 0 or self.board[coords[0]-1][coords[1]] == obstacle["id"])):
                move = False
        if(move):
            for o in self.obstacles:
                if(o["id"] == obstacle["id"]):
                    for i in range(len(obstacle["coords"])):
                        coords = obstacle["coords"][i]
                        self.board[coords[0]][coords[1]] = 0
                    for i in range(len(obstacle["coords"])):
                        coords = obstacle["coords"][i]
                        self.board[coords[0]-1][coords[1]] = obstacle["id"] 
                        obstacle["coords"][i] = [coords[0]-1, coords[1]] 
        return move 
    
    def check_end(self):
        if(self.obstacles[0]["coords"] == self.end_pos["coords"]):
            return True
        return False

    def eval_state(self):
        score = 0
        score = abs(pow((self.obstacles[0]["coords"][0][0] - self.end_pos["coords"][0][0]), 2) + (pow((self.obstacles[0]["coords"][0][1] - self.end_pos["coords"][0][1]), 2)))
        for obstacle in self.obstacles[1:]:
            score -= abs(pow((obstacle["coords"][0][0] - self.end_pos["coords"][0][0]), 2) + (pow((obstacle["coords"][0][1] - self.end_pos["coords"][0][1]), 2)))
        return score
    
    def describe(self, opt):
        for row in self.board:
            print(row)
        if(opt == "verbose"):
            print("\n Density of obstacles: ", self.density)
            print("\n Obstacles:")
            for obstacles in self.obstacles:
                print(obstacles) 
            print("\nHeuristic Params")
            print("h: ", self.h, ", g: ", self.g, ", f: ", self.f)
        print()
        return 0
