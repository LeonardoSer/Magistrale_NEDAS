#!/usr/bin/env python3
import copy
import csv
import pandas as pd
import chess
import math
import numpy as np
from chess_tools import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

MAPPING = {".":0, "p":1, "P":2, "r":3, "R":4, "n":5, "N":6, "b":7, "B":8, "q":9, "Q":10, "k":11, "K":12}
CHESSBOARD = [
        "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8",
        "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8",
        "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8",
        "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8",
        "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8",
        "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
        "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8",
        "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"
        ]

# genera un array dell possibili mosse sulla scacchiera
def gen_moves():
    moves = []
    for i in CHESSBOARD:
        for j in CHESSBOARD:
            if(i!=j):
              moves.append(i+j)
            if((i[1] == '2' and j[1] == '1') or (i[1] == '7' and j[1] == '8')):
                moves.append(i+j+'q')
    return moves 

# utilizza la posizione nell'array generato da gen_moves() per la codifica delle mosse
def encode_mv(mv):
    moves = gen_moves()
    if(len(str(mv))>4):
            mv = str(mv)[:4]+'q'
    return moves.index(str(mv))

# decodifica una mossa utilizzando l'array generato da gen_moves()
def decode_mv(enc_mv):
    moves = gen_moves()
    while(enc_mv > len(moves)-1):
        enc_mv -= 1
    return moves[enc_mv]

# crea un sample dalla board attuale, senza specificare la prossima mossa
def create_sample(board, depth, heuristics_ids):
    sample = []
    evaluation = boardEval(board, heuristics_ids)
    next_mv = ""
    board = make_matrix(board)
    
    for i in range(len(board)):
        for j in range(len(board)):
            sample.append(MAPPING[board[i][j]])
    
    sample.append(depth)
    sample.append(evaluation)
    return sample

# chiamata dopo ogni mossa della minmax, genera un sample e lo aggiunge al dataset
def add_sample_to_dataset(old_board, board, depth, heuristics_id):
    sample = []
    evaluation = boardEval(old_board, heuristics_id)
    board = make_matrix(board) 
    next_mv = ""
    
    for mv in old_board.legal_moves:
        tmp_board = copy.deepcopy(old_board)
        tmp_board.push(chess.Move.from_uci(str(mv)))
        tmp_board = make_matrix(tmp_board)
        equal = 1
        for i in range(len(board)):
            for j in range(len(board)):
                if(tmp_board[i][j] != board[i][j]):
                    equal = 0
        if(equal == 1):
            next_mv = str(mv)

    old_board = make_matrix(old_board) 
    
    for i in range(len(board)):
        for j in range(len(board)):
            sample.append(MAPPING[old_board[i][j]])
    
    sample.append(depth)
    sample.append(evaluation)
    sample.append(encode_mv(next_mv))
    append_to_csv(sample)

def append_to_csv(sample):
    row = []
    for el in sample:
        row.append(el)
 
    with open('dataset.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# crea, allena e valuta il regressore 
def model():
    columns = []
    for i in range(1,9):
        for j in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            columns.append(j+str(i))

    columns.append("depth")
    columns.append("eval")
    columns.append("next_mv")
    
    
    df = pd.read_csv("dataset.csv", names=columns) 
    print("\n", df)
    y = df["next_mv"]
    x = df.drop(["next_mv"], axis=1)
    x = x.apply(pd.to_numeric, errors='coerce')
    y = y.apply(pd.to_numeric, errors='coerce')
    TS_x, tst_x, TS_y, tst_y = train_test_split(x, y, test_size=0.2, train_size=0.8, shuffle=True)
    
    print("\nTS_x shape: ", TS_x.shape) 
    print("TS_y shape: ", TS_y.shape) 
    print("tst_x shape: ", tst_x.shape) 
    print("tst_y shape: ", tst_y.shape) 
        
    print("\nTraining regressor")
    regressor = LinearRegression().fit(TS_x, TS_y)
    print("training ended")

    predictions = regressor.predict(tst_x)
    score = mean_squared_error(predictions, tst_y)

    return regressor

# computa la mossa legale che più si avvicina alla predizione
def nearest_legal_mv(mv, board):
    nearest = None
    dist = float('inf') 
    for el in board.legal_moves:
        if(abs(encode_mv(el) - encode_mv(mv))<dist):
            nearest = el
            dist = abs(encode_mv(el) - encode_mv(mv))
    return nearest

# predice la prossima mossa tramite regressore
def regression(regressor, board, depth):
    sample = [create_sample(copy.deepcopy(board), depth, [1, 2])]
    next_mv = regressor.predict(sample)
    next_mv = decode_mv(int(math.sqrt(pow(next_mv, 2))))
    mvs = [str(mv) for mv in board.legal_moves]
    if(next_mv in mvs):
        return next_mv
    

    next_mv = nearest_legal_mv(next_mv, copy.deepcopy(board))
    return next_mv
