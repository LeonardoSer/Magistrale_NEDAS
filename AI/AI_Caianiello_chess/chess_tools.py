import os
import chess

MAPPING = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Ritorna una matrice dall'oggetto "board" della libreria chess
def make_matrix(board): #type(board) == chess.Board()
    pgn = board.epd()
    foo = []  #Final board
    pieces = pgn.split(" ", 1)[0]
    rows = pieces.split("/")
    for row in rows:
        foo2 = []  #This is the row I make
        for thing in row:
            if thing.isdigit():
                for i in range(0, int(thing)):
                    foo2.append('.')
            else:
                foo2.append(thing)
        foo.append(foo2)
    return foo

# Ritorna il valore associato alla confiurazione della board
def boardEval(board, heuristics_ids):
    
    score = 0
    piece_values = {'p': -1, 'b': -3, 'n': -3, 'r': -5, 'q': -9, 'k': -0,
            'P': 1, 'B': 3, 'N': 3, 'R': 5, 'Q': 9, 'K': 0}
    
    # migliora lo score rispetto il controllo che si ha sulla scacchiera 
    if(1 in heuristics_ids):
        if(board.turn):
            score += 10*board.legal_moves.count()
        else:
            score -= 10*board.legal_moves.count()
    
    mvs = [str(mv)[:4] for mv in board.legal_moves]
    turn = board.turn
    opp_k = ""
    board = make_matrix(board)
    
    # lo score migliora proporzionatamente al numero di pezzi che si hanno in più rispetto l'avversario
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] != '.'):
                score += piece_values[board[i][j]]
    
    # lo score migliora se il re avversario viene messo sotto scacco
    if(2 in heuristics_ids):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(turn):
                    if(board[i][j] == 'K'):
                        opp_k = str(MAPPING[i]) + str(j) 
                    for mv in mvs:
                        if(opp_k == mv[2:]):
                            score += 0.8
                else:
                    if(board[i][j] == 'k'):
                        opp_k = str(MAPPING[i]) + str(j) 
                    for mv in mvs:
                        if(opp_k == mv[2:]):
                            score -= 0.8
    return score

# Stampa sul terminale la board data in input
def display_board(board):
    os.system("clear")
    if(board.turn):
        print("White Turn")
    else:
        print("Black Turn")
    print(board, "\n")

