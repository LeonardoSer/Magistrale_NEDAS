#!/usr/bin/env python3
import chess
import time
import pygame
from chess_tools import *
from minmax_alpha_betha import *
from regressor import * 

PIXEL_SIZE = 80
SCREEN_H = PIXEL_SIZE*8 
SCREEN_W = PIXEL_SIZE*8
SCREEN_SIZE = (SCREEN_H, SCREEN_W)

# Definiamo alcuni colori
BOARD_COLOR = (169,169,169)

def get_rect(screen, x, y):
    return pygame.draw.rect(screen, BOARD_COLOR, [(SCREEN_H//2-(8*PIXEL_SIZE)//2)+PIXEL_SIZE*y, (SCREEN_W//2-(8*PIXEL_SIZE)//2)+PIXEL_SIZE*x, PIXEL_SIZE, PIXEL_SIZE], 0)

# funzione di gioco
def IA_play_chess(heuristics_ids, depth): 
    pygame.init()    
    
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("minmax alpha-beta chess")
    clock = pygame.time.Clock()
    
    path = []
    board = chess.Board() # iinizializza la board
    
    path.append(board) # contiene la sequenza di stati della partita giocata
    
    # creazione e training del regressore
    regressor = model()

    print("\nWhite player: regressor")
    print("Black player: minmax")
    print("\nPLAYING...")
    
    end = 0
    while not end: # finchè la board non è in una configurazione finale...
    
        if(board.is_game_over()):
            end = 1
        screen.fill(BOARD_COLOR)
        
        # creazione della scacchiera per il rendering
        for x in range(len(make_matrix(board))):
            for y in range(len(make_matrix(board)[x])):
            
                    # pedoni
                    if(make_matrix(board)[x][y] == 'P'):
                        rect = get_rect(screen, x, y)
                        img = pygame.image.load('images/P.png').convert()
                        img = pygame.transform.scale(img, (PIXEL_SIZE-2, PIXEL_SIZE-2))
                        screen.blit(img, rect)

                    if(make_matrix(board)[x][y] == 'p'):
                        rect = get_rect(screen, x, y)
                        img = pygame.image.load('images/p.png').convert()
                        img = pygame.transform.scale(img, (PIXEL_SIZE-2, PIXEL_SIZE-2))
                        screen.blit(img, rect)
                    
                    # torri
                    if(make_matrix(board)[x][y] == 'r'):
                        rect = get_rect(screen, x, y)
                        img = pygame.image.load('images/r.png').convert()
                        img = pygame.transform.scale(img, (PIXEL_SIZE-2, PIXEL_SIZE-2))
                        screen.blit(img, rect)
                    if(make_matrix(board)[x][y] == 'R'):
                        rect = get_rect(screen, x, y)
                        img = pygame.image.load('images/R.png').convert()
                        img = pygame.transform.scale(img, (PIXEL_SIZE-2, PIXEL_SIZE-2))
                        screen.blit(img, rect)

                    # cavalli
                    if(make_matrix(board)[x][y] == 'b'):
                        rect = get_rect(screen, x, y)
                        img = pygame.image.load('images/b.png').convert()
                        img = pygame.transform.scale(img, (PIXEL_SIZE-2, PIXEL_SIZE-2))
                        screen.blit(img, rect)
                    if(make_matrix(board)[x][y] == 'B'):
                        rect = get_rect(screen, x, y)
                        img = pygame.image.load('images/B.png').convert()
                        img = pygame.transform.scale(img, (PIXEL_SIZE-2, PIXEL_SIZE-2))
                        screen.blit(img, rect)
                    
                    # alfieri
                    if(make_matrix(board)[x][y] == 'n'):
                        rect = get_rect(screen, x, y)
                        img = pygame.image.load('images/n.png').convert()
                        img = pygame.transform.scale(img, (PIXEL_SIZE-2, PIXEL_SIZE-2))
                        screen.blit(img, rect)
                    if(make_matrix(board)[x][y] == 'N'):
                        rect = get_rect(screen, x, y)
                        img = pygame.image.load('images/N.png').convert()
                        img = pygame.transform.scale(img, (PIXEL_SIZE-2, PIXEL_SIZE-2))
                        screen.blit(img, rect)
                    
                    # regina
                    if(make_matrix(board)[x][y] == 'q'):
                        rect = get_rect(screen, x, y)
                        img = pygame.image.load('images/q.png').convert()
                        img = pygame.transform.scale(img, (PIXEL_SIZE-2, PIXEL_SIZE-2))
                        screen.blit(img, rect)
                    if(make_matrix(board)[x][y] == 'Q'):
                        rect = get_rect(screen, x, y)
                        img = pygame.image.load('images/Q.png').convert()
                        img = pygame.transform.scale(img, (PIXEL_SIZE-2, PIXEL_SIZE-2))
                        screen.blit(img, rect)
   
                    # re
                    if(make_matrix(board)[x][y] == 'k'):
                        rect = get_rect(screen, x, y)
                        img = pygame.image.load('images/k.png').convert()
                        img = pygame.transform.scale(img, (PIXEL_SIZE-2, PIXEL_SIZE-2))
                        screen.blit(img, rect)
                    if(make_matrix(board)[x][y] == 'K'):
                        rect = get_rect(screen, x, y)
                        img = pygame.image.load('images/K.png').convert()
                        img = pygame.transform.scale(img, (PIXEL_SIZE-2, PIXEL_SIZE-2))
                        screen.blit(img, rect)
    

        pygame.display.flip()
        clock.tick(20)
        

        # turni dei due giocatori 
        if not(end): 

            if not(board.turn):
                
                # codice per giocare tramite la minmax e ampliare il dataset
                old_board = copy.deepcopy(board)
                board = minmax_ab(board, depth, heuristics_ids) # esegue la mossa scelta dalla minmax search con alpha beta pruning
                add_sample_to_dataset(old_board, board, depth, heuristics_ids)
            
            else:
                # codice per giocare tramite il regressore
                next_mv = regression(regressor, board, depth) 
                board.push_uci(str(next_mv))
             
            path.append(board) # creiamo una storia della partita giocata rappresentata come array di board
    
    if(board.is_checkmate()):
        if(board.turn):
            print("\nBlack Won!\n")
        else:
            print("\nWhite Won!\n")
    
    print("is checkmate? ", board.is_checkmate())
    print("is stalemate? ", board.is_stalemate())
    print("is seventyfive_moves? ", board.is_seventyfive_moves())
    print("is fivefold repetition? ", board.is_fivefold_repetition())
    print("is insufficient material? ", board.is_insufficient_material())
    
    print("\n60 second to exit...")
    
    time.sleep(60)
    pygame.quit()
    
    return path

# giochiamo e otteniamo il path degli stati della board
depth = 3
heuristic = [1,2]
path = IA_play_chess(heuristic, depth)
