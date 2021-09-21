import math
import copy
import chess
from chess_tools import *

# genera tutte le possibilì configurazioni a cui porterebe una mossa sulla scacchiera
def childs(board):
    childs = []
    for mv in board.legal_moves:
        tmp_board = copy.deepcopy(board)
        move = chess.Move.from_uci(str(mv))
        tmp_board.push(move)
        childs.append(tmp_board)
    return childs

# performa una minmax search con alpha-betha pruning a partire da una configurazione della scacchiera
def minmax_search_ab(node, a, b, depth, best_mv, heuristic_ids):
    
    #condizione di base
    if(depth == 0 or node.is_checkmate()):
        return {"node": node, "eval": boardEval(node, heuristic_ids)}
    
    # turno del maximizer
    if(node.turn):
        maxEval = -math.inf
        for child in childs(node):
            elem = minmax_search_ab(child, a, b, depth-1, best_mv, heuristic_ids)
            evaluation = elem["eval"]
            maxEval = max(maxEval, evaluation)
            
            # aggiorna ricorsivamente la configurazione migliore a cui una mossa del maximizer può portare
            if(maxEval == evaluation):
                best_mv = elem["node"]
                 
            # alpha-beta pruning
            a = max(a, evaluation)
            if(b <= a):
                break
        return {"node": node, "eval": maxEval, "best-child": best_mv}
    # turno del minimizer
    else:
        minEval = math.inf
        for child in childs(node):
            elem = minmax_search_ab(child, a, b, depth-1, best_mv, heuristic_ids)
            evaluation = elem["eval"]
            minEval = min(minEval, evaluation)
         
            # aggiorna ricorsivamente la configurazione migliore a cui una mossa del minimizer può portare
            if(minEval == evaluation):
                best_mv = elem["node"]
            
            # alpha-beta pruning
            b = min(b, evaluation)
            if(b <= a):
                break
        return {"node": node, "eval": minEval, "best-child": best_mv}

# Interfaccia per minmax_search_ab_(), riduce il numero di parametri necessari alla chiamata
def minmax_ab(board, depth, heuristics_ids):
    return minmax_search_ab(board, -math.inf, math.inf, depth, board, heuristics_ids)["best-child"]

