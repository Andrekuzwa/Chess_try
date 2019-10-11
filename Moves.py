from typing import List, Any, Union

import numpy as np
from Board import *
import pprint


def array64_to_array120(board64):
    board_10x12 = [0 for i in range(120)]
    for i in range(8):
        board_10x12[i + 21] = board64[i]
    for i in range(8):
        board_10x12[i + 31] = board64[i+8]
    for i in range(8):
        board_10x12[i + 41] = board64[i+16]
    for i in range(8):
        board_10x12[i + 51] = board64[i+24]
    for i in range(8):
        board_10x12[i + 61] = board64[i+32]
    for i in range(8):
        board_10x12[i + 71] = board64[i+40]
    for i in range(8):
        board_10x12[i + 81] = board64[i+48]
    for i in range(8):
        board_10x12[i + 91] = board64[i+56]
    board_10x12 = np.asarray(board_10x12)
    return board_10x12


def array120_to_array64(board_10x12):
    board64 = [0 for i in range(64)]
    for i in range(8):
        board64[i] = board_10x12[i + 21]
    for i in range(8):
        board64[i + 8] = board_10x12[i + 31]
    for i in range(8):
        board64[i + 16] = board_10x12[i + 41]
    for i in range(8):
        board64[i + 24] = board_10x12[i + 51]
    for i in range(8):
        board64[i + 32] = board_10x12[i + 61]
    for i in range(8):
        board64[i + 40] = board_10x12[i + 71]
    for i in range(8):
        board64[i + 48] = board_10x12[i + 81]
    for i in range(8):
        board64[i + 56] = board_10x12[i + 91]
    board64 = np.asarray(board64)
    return board64


#awoduhawuodhawhdoawhdhwadawd

class Pawn(Board):

    def __init__(self,boardState,WP,BP,W_ALL,B_ALL):
        self.WP = WP
        self.BP = BP
        self.W_ALL = W_ALL
        self.B_ALL = B_ALL
        self.boardState = boardState

    def whitePawnAttMap(self):
        board120 = array64_to_array120(self.WP)
        att120 = np.array([0 for i in range(120)])
        for i in range(120):
            if board120[i] == 1:
                att120[i-9] = 1
                att120[i-11] = 1
        att120 = array120_to_array64(att120)
        return att120

    def blackPawnAttMap(self):
        board120 = array64_to_array120(self.BP)
        att120 = np.array([0 for i in range(120)])
        for i in range(120):
            if board120[i] == 1:
                att120[i+9] = 1
                att120[i+11] = 1
        att120 = array120_to_array64(att120)
        return att120\

    def PLmoves_whitePawns(self):
        board120 = array64_to_array120(self.WP)

        move_list = []
        for i in board120:
            if board120[i] == 1:







class Night(Board):
    def __init__(self,boardState,WN,BN):
        self.WN = WN
        self.BN = BN
        self.boardState = boardState

    def whiteNightAttMap(self):
        board120 = array64_to_array120(self.WN)
        att120 = np.array([0 for i in range(120)])
        for i in range(120):
            if board120[i] == 1:
                att120[i-8] = 1
                att120[i-12] = 1
                att120[i-19] = 1
                att120[i-21] = 1
                att120[i + 8] = 1
                att120[i + 12] = 1
                att120[i + 19] = 1
                att120[i + 21] = 1
        att120 = array120_to_array64(att120)
        return att120

    def blackNightAttMap(self):
        board120 = array64_to_array120(self.BN)
        att120 = np.array([0 for i in range(120)])
        for i in range(120):
            if board120[i] == 1:
                att120[i - 8] = 1
                att120[i - 12] = 1
                att120[i - 19] = 1
                att120[i - 21] = 1
                att120[i + 8] = 1
                att120[i + 12] = 1
                att120[i + 19] = 1
                att120[i + 21] = 1
        att120 = array120_to_array64(att120)
        return att120

class Bishop(Board):
    def __init__(self, boardState, WB, BB):
        self.WB = WB
        self.BB = BB
        self.boardState = boardState

    def whiteBishopAttMap(self):
        board120 = array64_to_array120(self.WB)
        att120 = np.array([0 for i in range(120)])
        att_index = []
        for i in range(len(board120)):
            if board120[i] == 1:
                for j in range(9,72,9):
                    if i+j in in_index:
                        att_index.append(i+j)
                    else:
                        break
                for j in range(11,88,11):
                    if i+j in in_index:
                        att_index.append(i+j)
                    else:
                        break
                for j in range(-9,-72,-9):
                    if i+j in in_index:
                        att_index.append(i+j)
                    else:
                        break
                for j in range(-11,-88,-11):
                    if i+j in in_index:
                        att_index.append(i+j)
                    else:
                        break
        for i in att_index:
            att120[i] = 1
        att120 = array120_to_array64(att120)
        return att120

    def blackBishopAttMap(self):
        board120 = array64_to_array120(self.BB)
        att120 = np.array([0 for i in range(120)])
        att_index = []
        for i in range(len(board120)):
            if board120[i] == 1:
                for j in range(9, 72, 9):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(11, 88, 11):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(-9, -72, -9):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(-11, -88, -11):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
        for i in att_index:
            att120[i] = 1
        att120 = array120_to_array64(att120)
        return att120


class Rook(Board):
    def __init__(self, boardState, WR, BR):
        self.WR = WR
        self.BR = BR
        self.boardState = boardState

    def whiteRookAttMap(self):
        board120 = array64_to_array120(self.WR)
        att120 = np.array([0 for i in range(120)])
        att_index = []

        for i in range(len(board120)):
            if board120[i] == 1:
                for j in range(-10,-80,-10):
                    if i+j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(10,80,10):
                    if i+j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(1,8):
                    if i+j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(-1,-8,-1):
                    if i+j in in_index:
                        att_index.append(i + j)
                    else:
                        break
        for i in att_index:
            att120[i] = 1
        att120 = array120_to_array64(att120)
        return att120

    def blackRookAttMap(self):
        board120 = array64_to_array120(self.BR)
        att120 = np.array([0 for i in range(120)])
        att_index = []

        for i in range(len(board120)):
            if board120[i] == 1:
                for j in range(-10, -80, -10):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(10, 80, 10):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(1, 8):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(-1, -8, -1):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
        for i in att_index:
            att120[i] = 1
        att120 = array120_to_array64(att120)
        return att120


class Queen(Board):
    def __init__(self, boardState, WQ, BQ):
        self.WQ = WQ
        self.BQ = BQ
        self.boardState = boardState

    def whiteQueenAttMap(self):
        board120 = array64_to_array120(self.WQ)
        att120 = np.array([0 for i in range(120)])
        att_index = []

        for i in range(len(board120)):
            if board120[i] == 1:
                for j in range(-10, -80, -10):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(10, 80, 10):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(1, 8):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(-1, -8, -1):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(9, 72, 9):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(11, 88, 11):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(-9, -72, -9):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(-11, -88, -11):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
        for i in att_index:
            att120[i] = 1
        att120 = array120_to_array64(att120)
        return att120


    def blackQueenAttMap(self):
        board120 = array64_to_array120(self.BQ)
        att120 = np.array([0 for i in range(120)])
        att_index = []

        for i in range(len(board120)):
            if board120[i] == 1:
                for j in range(-10, -80, -10):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(10, 80, 10):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(1, 8):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(-1, -8, -1):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(9, 72, 9):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(11, 88, 11):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(-9, -72, -9):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
                for j in range(-11, -88, -11):
                    if i + j in in_index:
                        att_index.append(i + j)
                    else:
                        break
        for i in att_index:
            att120[i] = 1
        att120 = array120_to_array64(att120)
        return att120

class King(Board):
    def __init__(self, boardState, WK, BK):
        self.WK = WK
        self.BK = BK
        self.boardState = boardState

    def whiteKingAttMap(self):
        board120 = array64_to_array120(self.WK)
        att120 = np.array([0 for i in range(120)])
        for i in range(len(board120)):
            if board120[i] == 1:
                att120[i-11] = 1
                att120[i - 10] = 1
                att120[i - 9] = 1
                att120[i - 1] = 1
                att120[i + 11] = 1
                att120[i + 10] = 1
                att120[i + 9] = 1
                att120[i + 1] = 1
        att120 = array120_to_array64(att120)
        return att120

    def blackKingAttMap(self):
        board120 = array64_to_array120(self.BK)
        att120 = np.array([0 for i in range(120)])
        for i in range(len(board120)):
            if board120[i] == 1:
                att120[i-11] = 1
                att120[i - 10] = 1
                att120[i - 9] = 1
                att120[i - 1] = 1
                att120[i + 11] = 1
                att120[i + 10] = 1
                att120[i + 9] = 1
                att120[i + 1] = 1
        att120 = array120_to_array64(att120)
        return att120















p = Pawn(b.get_board_state(),b.WP,b.BP)
n = Night(b.get_board_state(),b.WN,b.BN)
# b = Bishop(b.get_board_state(),b.WB,b.BB)
r = Rook(b.get_board_state(),b.WR,b.BR)
q = Queen(b.get_board_state(),b.WQ,b.WQ)
k = King(b.get_board_state(),b.WK,b.WK)
k.Display(k.whiteKingAttMap())
# print(wp.whitePawnAttMap())
# print(wp.blackPawnAttMap())






