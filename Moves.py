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
        self.PLmoves_whitePawn = self.PLmoves_whitePawnDef()
        self.PLmoves_blackPawn = self.PLmoves_blackPawnDef()

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
        board120 = array64_to_array120(self.OB.BP)
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
        whitePieces120 = array64_to_array120(self.OB.W_ALL)
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
        board120 = array64_to_array120(self.OB.BP)
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

    def __init__(self, OB,whiteNightAttMap = [],blackNightAttMap = [],PLmoves_whiteNight = [],PLmoves_blackNight = []):
        self.OB = OB
        self.whiteNightAttMap = self.whiteNightAttMapDef()
        self.blackNightAttMap = self.blackNightAttMapDef()
        self.PLmoves_whiteNight = self.PLmoves_whiteNightDef()
        self.PLmoves_blackNight = self.PLmoves_blackNightDef()

    def whiteNightAttMapDef(self):
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

    def blackNightAttMapDef(self):
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

    def PLmoves_whiteNightDef(self):
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

    def PLmoves_blackNightDef(self):
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
    def __init__(self, OB, whiteBishopAttMap = [],blackBishopAttMap = [],PLmoves_whiteBishop = [],PLmoves_blackBishop = []):
        self.OB = OB
        self.whiteBishopAttMap = self.whiteBishopAttMapDef()
        self.blackBishopAttMap = self.blackBishopAttMapDef()
        self.PLmoves_whiteBishop = self.PLmoves_whiteBishopDef()
        self.PLmoves_blackBishop = self.PLmoves_blackBishopDef()

    def whiteBishopAttMapDef(self):
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

    def blackBishopAttMapDef(self):
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

    def PLmoves_whiteBishopDef(self):
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

    def PLmoves_blackBishopDef(self):
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
    def __init__(self, OB,whiteRookAttMap = [],blackRookAttMap = [],PLmoves_whiteRook = [],PLmoves_blackRook = []):
        self.OB = OB
        self.whiteRookAttMap = self.whiteRookAttMapDef()
        self.blackRookAttMap = self.blackRookAttMapDef()
        self.PLmoves_whiteRook = self.PLmoves_whiteRookDef()
        self.PLmoves_blackRook = self.PLmoves_blackRookDef()

    def whiteRookAttMapDef(self):
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

    def blackRookAttMapDef(self):
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

    def PLmoves_whiteRookDef(self):
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

    def PLmoves_blackRookDef(self):
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
    def __init__(self, OB,whiteQueenAttMap = [],blackQueenAttMap = [],PLmoves_whiteQueen = [],PLmoves_blackQueen = []):
        self.OB = OB
        self.whiteQueenAttMap = self.whiteQueenAttMapDef()
        self.blackQueenAttMap = self.blackQueenAttMapDef()
        self.PLmoves_whiteQueen = self.PLmoves_whiteQueenDef()
        self.PLmoves_blackQueen = self.PLmoves_blackQueenDef()

    def whiteQueenAttMapDef(self):
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

    def blackQueenAttMapDef(self):
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

    def PLmoves_whiteQueenDef(self):
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

    def PLmoves_blackQueenDef(self):
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

class King(Board):
    def __init__(self, OB,pawn_object,whiteKingAttMap = [],blackKingAttMap = [],PLmoves_whiteKing = [],PLmoves_blackKing = []):
        self.OB = OB
        self.pawn_object = pawn_object
        self.whiteKingAttMap = self.whiteKingAttMaDef()
        self.blackKingAttMap = self.blackKingAttMapDef()
        self.PLmoves_whiteKing = self.PLmoves_whiteKingDef()
        self.PLmoves_blackKing = self.PLmoves_blackKingDef()

    def whiteKingAttMaDef(self):
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

    def blackKingAttMapDef(self):
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

    def PLmoves_whiteKingDef(self):
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

    def PLmoves_blackKingDef(self):
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
        moves = []
        if self.OB.WK_moved == True:
            self.OB.WSC = False
            self.OB.WLC = False
        if self.OB.WSR_moved == True:
            self.OB.WSC = False
        if self.OB.WLR_moved == True:
            self.OB.WLC = False
        if self.OB.ALL[61] == 0 and self.OB.ALL[62] == 0 and\
                (96 not in [item[1] for item in self.OB.B_PLmoves]) and\
                (97 not in [item[1] for item in self.OB.B_PLmoves]) and\
                self.pawn_object.blackPawnAttMap[61] == 0 and\
                self.pawn_object.blackPawnAttMap[62] == 0 and\
                self.OB.WK_checked == False:
            moves.append((95,97))
        if self.OB.ALL[57] == 0 and self.OB.ALL[58] == 0 and self.OB.ALL[59] == 0 and\
                (92 not in [item[1] for item in self.OB.B_PLmoves]) and\
                (93 not in [item[1] for item in self.OB.B_PLmoves]) and\
                (94 not in [item[1] for item in self.OB.B_PLmoves]) and\
                self.pawn_object.blackPawnAttMap[57] == 0 and\
                self.pawn_object.blackPawnAttMap[58] == 0 and\
                self.pawn_object.blackPawnAttMap[59] == 0 and\
                self.OB.WK_checked == False:
            moves.append((95,93))
        return moves

    def blackCastleCheck(self):
        moves = []
        if self.OB.BK_moved == True:
            self.OB.BSC = False
            self.OB.BLC = False
        if self.OB.BSR_moved == True:
            self.OB.BSC = False
        if self.OB.BLR_moved == True:
            self.OB.BLC = False
        if self.OB.ALL[5] == 0 and self.OB.ALL[6] == 0 and\
                (26 not in [item[1] for item in self.OB.W_PLmoves]) and\
                (27 not in [item[1] for item in self.OB.W_PLmoves]) and\
                self.pawn_object.whitePawnAttMap[5] == 0 and\
                self.pawn_object.whitePawnAttMap[6] == 0 and\
                self.OB.BK_checked == False:
            moves.append((25,27))
        if self.OB.ALL[1] == 0 and self.OB.ALL[2] == 0 and self.OB.ALL[3] == 0 and\
                (22 not in [item[1] for item in self.OB.W_PLmoves]) and\
                (23 not in [item[1] for item in self.OB.W_PLmoves]) and\
                (24 not in [item[1] for item in self.OB.W_PLmoves]) and\
                self.pawn_object.whitePawnAttMap[1] == 0 and\
                self.pawn_object.whitePawnAttMap[2] == 0 and\
                self.pawn_object.whitePawnAttMap[3] == 0 and\
                self.OB.BK_checked == False:
            moves.append((25,23))
        return moves










p = Pawn(b)
k = King(b,p)
n = Night(b)
B = Bishop(b)
r = Rook(b)
q  = Queen(b)

print(k.whiteKingAttMap)
print(k.blackKingAttMap)
print(k.PLmoves_blackKing)
print(k.PLmoves_whiteKing)







