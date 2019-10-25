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

#OB - OBJECT BOARD
class Pawn(Board):
    def __init__(self,OB,whitePawnAttMap = [],blackPawnAttMap = [],PLmoves_whitePawn = [],PLmoves_blackPawn = []):
        self.OB = OB
        self.whitePawnAttMap = self.whitePawnAttMapDef()
        self.blackPawnAttMap = self.blackPawnAttMapDef()
        self.PLmoves_whitePawn = self.blackPawnAttMapDef()
        self.PLmoves_blackPawn = self.blackPawnAttMapDef()

    def whitePawnAttMapDef(self):
        board120 = array64_to_array120(self.OB.WP)
        att120 = np.array([0 for i in range(120)])
        for i in range(120):
            if board120[i] == 1:
                att120[i-9] = 1
                att120[i-11] = 1
        att120 = array120_to_array64(att120)
        return att120

    def blackPawnAttMapDef(self):
        board120 = array64_to_array120(self.BP)
        att120 = np.array([0 for i in range(120)])
        for i in range(120):
            if board120[i] == 1:
                att120[i+9] = 1
                att120[i+11] = 1
        att120 = array120_to_array64(att120)
        return att120\

    def PLmoves_whitePawnDef(self):
        board120 = array64_to_array120(self.OB.WP)
        blackPieces120 = array64_to_array120(self.OB.B_ALL)
        whitePieces120 = array64_to_array120(self.W_ALL)
        move_list = []
        for i in range(120):
            if board120[i] == 1:
                if blackPieces120[i-11] == 1 and i-11 in in_index:
                    move_list.append((i,i-11))
                if blackPieces120[i-9] == 1 and i-9 in in_index:
                    move_list.append((i,i-9))
                if (blackPieces120 | whitePieces120)[i-10]== 0 and i-10 in in_index:
                    move_list.append((i,i-10))
                if i in FILE_2 and (blackPieces120 | whitePieces120)[i-10]==0 and (blackPieces120 | whitePieces120)[i-20]==0 and  i-20 in in_index:
                    move_list.append((i,i-20))
        return move_list

    def PLmoves_blackPawnDef(self):
        board120 = array64_to_array120(self.OB.OB.BP)
        blackPieces120 = array64_to_array120(self.OB.B_ALL)
        whitePieces120 = array64_to_array120(self.OB.W_ALL)
        move_list = []
        for i in range(120):
            if board120[i] == 1:
                if whitePieces120[i + 11] == 1 and i + 11 in in_index:
                    move_list.append((i, i + 11))
                if whitePieces120[i + 9] == 1 and i + 9 in in_index:
                    move_list.append((i, i + 9))
                if (blackPieces120 | whitePieces120)[i + 10] == 0 and i + 10 in in_index:
                    move_list.append((i, i + 10))
                if i in FILE_7 and (blackPieces120 | whitePieces120)[i+10]==0 and (blackPieces120 | whitePieces120)[i+20]==0and  i+20 in in_index:
                    move_list.append((i, i + 20))
        return move_list

class Night(Board):

    def __init__(self, OB):
        self.OB = OB

    def whiteNightAttMap(self):
        board120 = array64_to_array120(self.OB.WN)
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
        board120 = array64_to_array120(self.OB.BN)
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

    def PLmoves_whiteNight(self):
        board120 = array64_to_array120(self.OB.WN)
        blackPieces120 = array64_to_array120(self.OB.B_ALL)
        whitePieces120 = array64_to_array120(self.OB.W_ALL)
        move_list = []
        for i in range(120):
            if board120[i] == 1:
                if blackPieces120[i-8] == 1 or whitePieces120[i-8] == 0 and i-8 in in_index:
                    move_list.append((i,i-8))
                if blackPieces120[i-12] == 1 or whitePieces120[i-12] == 0 and i-12 in in_index:
                    move_list.append((i,i-12))
                if blackPieces120[i-19] == 1 or whitePieces120[i-19] == 0 and i-19 in in_index:
                    move_list.append((i,i-19))
                if blackPieces120[i-21] == 1 or whitePieces120[i-21] == 0 and i-21 in in_index:
                    move_list.append((i,i-21))
                if blackPieces120[i + 8] == 1 or whitePieces120[i + 8] == 0 and i+8 in in_index:
                    move_list.append((i, i + 8))
                if blackPieces120[i + 12] == 1 or whitePieces120[i + 12] == 0 and i+12 in in_index:
                    move_list.append((i, i + 12))
                if blackPieces120[i + 19] == 1 or whitePieces120[i + 19] == 0 and i+19 in in_index:
                    move_list.append((i, i + 19))
                if blackPieces120[i + 21] == 1 or whitePieces120[i + 21] == 0 and i+21 in in_index:
                    move_list.append((i, i + 21))
        return move_list

    def PLmoves_blackNight(self):
        board120 = array64_to_array120(self.OB.BN)
        blackPieces120 = array64_to_array120(self.OB.B_ALL)
        whitePieces120 = array64_to_array120(self.OB.W_ALL)
        move_list = []
        for i in range(120):
            if board120[i] == 1:
                if whitePieces120[i - 8] == 1 or blackPieces120[i - 8] == 0 and i - 8 in in_index:
                    move_list.append((i, i - 8))
                if  whitePieces120[i - 12] == 1 or blackPieces120[i - 12] == 0 and i - 12 in in_index:
                    move_list.append((i, i - 12))
                if   whitePieces120[i - 19] == 1 or blackPieces120[i - 19] == 0 and i - 19 in in_index:
                    move_list.append((i, i - 19))
                if   whitePieces120[i - 21] == 1 or blackPieces120[i - 21] == 0 and i - 21 in in_index:
                    move_list.append((i, i - 21))
                if   whitePieces120[i + 8] == 1 or blackPieces120[i + 8] == 0 and i + 8 in in_index:
                    move_list.append((i, i + 8))
                if   whitePieces120[i + 12] == 1 or blackPieces120[i + 12] == 0 and i + 12 in in_index:
                    move_list.append((i, i + 12))
                if   whitePieces120[i + 19] == 1 or blackPieces120[i + 19] == 0 and i + 19 in in_index:
                    move_list.append((i, i + 19))
                if  whitePieces120[i + 21] == 1 or blackPieces120[i + 21] == 0  and i + 21 in in_index:
                    move_list.append((i, i + 21))
        return move_list

class Bishop(Board):
    def __init__(self, OB):
        self.OB = OB

    def whiteBishopAttMap(self):
        board120 = array64_to_array120(self.OB.WB)
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
        board120 = array64_to_array120(self.OB.BB)
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

    def PLmoves_whiteBishop(self):
        board120 = array64_to_array120(self.OB.WB)
        blackPieces120 = array64_to_array120(self.OB.B_ALL)
        whitePieces120 = array64_to_array120(self.OB.W_ALL)
        move_list = []
        for i in range(len(board120)):
            if board120[i] == 1:
                for j in range(9, 72, 9):
                    if i+j in in_index:
                        if (whitePieces120 | blackPieces120)[i+j] == 0:
                            move_list.append((i,i+j))
                        elif blackPieces120[i+j] == 1:
                            move_list.append((i,i+j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(11, 88, 11):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif blackPieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(-9, -72, -9):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif blackPieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(-11, -88, -11):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif blackPieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
        return move_list

    def PLmoves_blackBishop(self):
        board120 = array64_to_array120(self.OB.BB)
        blackPieces120 = array64_to_array120(self.OB.B_ALL)
        whitePieces120 = array64_to_array120(self.OB.W_ALL)
        move_list = []
        for i in range(len(board120)):
            if board120[i] == 1:
                for j in range(9, 72, 9):
                    if i+j in in_index:
                        if (whitePieces120 | blackPieces120)[i+j] == 0:
                            move_list.append((i,i+j))
                        elif whitePieces120[i+j] == 1:
                            move_list.append((i,i+j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(11, 88, 11):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif whitePieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(-9, -72, -9):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif whitePieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(-11, -88, -11):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif whitePieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
        return move_list

class Rook(Board):
    def __init__(self, OB):
        self.OB = OB

    def whiteRookAttMap(self):
        board120 = array64_to_array120(self.OB.WR)
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
        board120 = array64_to_array120(self.OB.BR)
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

    def PLmoves_whiteRook(self):
        board120 = array64_to_array120(self.OB.WR)
        blackPieces120 = array64_to_array120(self.OB.B_ALL)
        whitePieces120 = array64_to_array120(self.OB.W_ALL)
        move_list = []
        for i in range(len(board120)):
            if board120[i] == 1:
                for j in range(-10, -80, -10):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif blackPieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(10, 80, 10):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif blackPieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(1, 8):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif blackPieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(-1, -8, -1):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif blackPieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
        return move_list

    def PLmoves_blackRook(self):
        board120 = array64_to_array120(self.OB.BR)
        blackPieces120 = array64_to_array120(self.OB.B_ALL)
        whitePieces120 = array64_to_array120(self.OB.W_ALL)
        move_list = []
        for i in range(len(board120)):
            if board120[i] == 1:
                for j in range(-10, -80, -10):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif whitePieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(10, 80, 10):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif whitePieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(1, 8):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif whitePieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(-1, -8, -1):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif whitePieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
        return move_list

class Queen(Board):
    def __init__(self, OB):
        self.OB = OB

    def whiteQueenAttMap(self):
        board120 = array64_to_array120(self.OB.WQ)
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
        board120 = array64_to_array120(self.OB.BQ)
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

    def PLmoves_whiteQueen(self):
        board120 = array64_to_array120(self.OB.WQ)
        blackPieces120 = array64_to_array120(self.OB.B_ALL)
        whitePieces120 = array64_to_array120(self.OB.W_ALL)
        move_list = []
        for i in range(len(board120)):
            if board120[i] == 1:
                for j in range(-10, -80, -10):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif blackPieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(10, 80, 10):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif blackPieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(1, 8):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif blackPieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(-1, -8, -1):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif blackPieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(9, 72, 9):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif blackPieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(11, 88, 11):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif blackPieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(-9, -72, -9):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif blackPieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(-11, -88, -11):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif blackPieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
        return move_list

    def PLmoves_blackQueen(self):
        board120 = array64_to_array120(self.OB.BQ)
        blackPieces120 = array64_to_array120(self.OB.B_ALL)
        whitePieces120 = array64_to_array120(self.OB.W_ALL)
        move_list = []
        for i in range(len(board120)):
            if board120[i] == 1:
                for j in range(-10, -80, -10):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif whitePieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(10, 80, 10):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif whitePieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(1, 8):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif whitePieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(-1, -8, -1):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif whitePieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(9, 72, 9):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif whitePieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(11, 88, 11):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif whitePieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(-9, -72, -9):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif whitePieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
                for j in range(-11, -88, -11):
                    if i + j in in_index:
                        if (whitePieces120 | blackPieces120)[i + j] == 0:
                            move_list.append((i, i + j))
                        elif whitePieces120[i + j] == 1:
                            move_list.append((i, i + j))
                            break
                        else:
                            break
                    else:
                        break
        return move_list

class King(Board,Pawn):
    def __init__(self, OB):
        self.OB = OB

    def whiteKingAttMap(self):
        board120 = array64_to_array120(self.OB.WK)
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
        board120 = array64_to_array120(self.OB.BK)
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

    def PLmoves_whiteKing(self):
        board120 = array64_to_array120(self.OB.WK)
        blackPieces120 = array64_to_array120(self.OB.B_ALL)
        whitePieces120 = array64_to_array120(self.OB.W_ALL)
        move_list = []
        for i in range(120):
            if board120[i] == 1:
                if blackPieces120[i - 1] == 1 or whitePieces120[i - 1] == 0 and i - 1 in in_index:
                    move_list.append((i, i - 1))
                if blackPieces120[i - 9] == 1 or whitePieces120[i - 9] == 0 and i - 9 in in_index:
                    move_list.append((i, i - 9))
                if blackPieces120[i - 10] == 1 or whitePieces120[i - 10] == 0 and i - 10 in in_index:
                    move_list.append((i, i - 10))
                if blackPieces120[i - 11] == 1 or whitePieces120[i - 11] == 0 and i - 1 in in_index:
                    move_list.append((i, i - 11))
                if blackPieces120[i + 1] == 1 or whitePieces120[i + 1] == 0 and i + 1 in in_index:
                    move_list.append((i, i + 1))
                if blackPieces120[i + 9] == 1 or whitePieces120[i + 9] == 0 and i + 9 in in_index:
                    move_list.append((i, i + 9))
                if blackPieces120[i + 10] == 1 or whitePieces120[i + 10] == 0 and i + 10 in in_index:
                    move_list.append((i, i + 10))
                if blackPieces120[i + 11] == 1 or whitePieces120[i + 1] == 0 and i + 11 in in_index:
                    move_list.append((i, i + 11))
        return move_list

    def PLmoves_blackKing(self):
        board120 = array64_to_array120(self.OB.BK)
        blackPieces120 = array64_to_array120(self.OB.B_ALL)
        whitePieces120 = array64_to_array120(self.OB.W_ALL)
        move_list = []
        for i in range(120):
            if board120[i] == 1:
                if whitePieces120[i - 1] == 1 or blackPieces120[i - 1] == 0 and i - 1 in in_index:
                    move_list.append((i, i - 1))
                if whitePieces120[i - 9] == 1 or blackPieces120[i - 9] == 0 and i - 9 in in_index:
                    move_list.append((i, i - 9))
                if whitePieces120[i - 10] == 1 or blackPieces120[i - 10] == 0 and i - 10 in in_index:
                    move_list.append((i, i - 10))
                if whitePieces120[i - 11] == 1 or blackPieces120[i - 11] == 0 and i - 11 in in_index:
                    move_list.append((i, i - 11))
                if whitePieces120[i + 1] == 1 or blackPieces120[i + 1] == 0 and i + 1 in in_index:
                    move_list.append((i, i + 1))
                if whitePieces120[i + 9] == 1 or blackPieces120[i + 9] == 0 and i + 9 in in_index:
                    move_list.append((i, i + 9))
                if whitePieces120[i + 10] == 1 or blackPieces120[i + 10] == 0 and i + 10 in in_index:
                    move_list.append((i, i + 10))
                if whitePieces120[i + 1] == 1 or blackPieces120[i + 11] == 0 and i + 11 in in_index:
                    move_list.append((i, i + 11))
        return move_list

    def whiteCastleCheck(self):
        if self.OB.WK_moved == True:
            self.OB.WSC = False
            self.OB.WLC = False
        if self.OB.WSR_moved == True:
            self.OB.WSC = False
        if self.OB.WLR_moved == True:
            self.OB.WLC = False
        if self.OB.ALL[61] == 1 or self.OB.ALL[62] == 1:
            self.OB.WSC = False
        if self.OB.ALL[57] == 1 or self.OB.ALL[58] == 1 or self.OB.ALL[59] == 1:
            self.OB.WLC = False
        if (96 in [item[1] for item in self.OB.B_Pmoves]) or (97 in [item[1] for item in self.OB.B_Pmoves]) or self.OB.blackPawnAttMap()[61] == 1 or self.OB.blackPawnAttMap()[62] == 1:




        






k = King(b)







