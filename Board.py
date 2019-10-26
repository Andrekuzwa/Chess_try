import numpy as np
# a = '00000011'
# b = '00000010'
# a_int = int(a,2)
# b_int = int(b,2)
# c = a_int & b_int
# print(a_int,b_int,c)
# print('{0:b}'.format(c))
# print()
# start_board =       np.array([['r','n','b','q','k','b','n','r'],
#                               ['p','p','p','p','p','p','p','p'],
#                               [' ',' ',' ',' ',' ',' ',' ',' '],
#                               [' ',' ',' ',' ',' ',' ',' ',' '],
#                               [' ',' ',' ',' ','p',' ',' ',' '],
#                               [' ',' ',' ',' ',' ',' ',' ',' '],
#                               ['P','P','P','P','P','P','P','P'],
#                               ['R','N','B','Q','K','B','N','R']])
#
# # start_board = np.reshape(start_board,64)
# # board_10x12 = np.array(['' for i in range(120)])
# # for i in range(64):
# #     board_10x12[i+21] = start_board[i]
#
# WP,WN, WB, WR, WQ, WK, BP, BN, BB, BR, BQ, BK, ALL = [],[],[],[],[],[],[],[],[],[],[],[],[]
#
#
#
#

in_index = [21,22,23,24,25,26,27,28,31,32,33,34,35,36,37,38,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,58,61,62,63,64,65,66,67,68,71,72,73,74,75,76,77,78,81,82,83,84,85,86,87,88,91,92,93,94,95,96,97,98]

# h1,h2,h3,h4,h5,h6,h7,h8 = 21,22,23,24,25,26,27,28
# g1,g2,g3,g4,g5,g6,g7,g8 = 31,32,33,34,35,36,37,38
# f1,f2,f3,f4,f5,f6,f7,f8 = 41,42,43,44,45,46,47,48
# e1,e2,e3,e4,e5,e6,e7,e8 = 51,52,53,54,55,56,57,58
# d1,d2,d3,d4,d5,d6,d7,d8 = 61,62,63,64,65,66,67,68
# c1,c2,c3,c4,c5,c6,c7,c8 = 71,72,73,74,75,76,77,78
# b1,b2,b3,b4,b5,b6,b7,b8 = 81,82,83,84,85,86,87,88
# a1,a2,a3,a4,a5,a6,a7,a8 = 91,92,93,94,95,96,97,98

FILE_8 = [21,22,23,24,25,26,27,28]
FILE_7 = [31,32,33,34,35,36,37,38]
FILE_6 = [41,42,43,44,45,46,47,48]
FILE_5 = [51,52,53,54,55,56,57,58]
FILE_4 = [61,62,63,64,65,66,67,68]
FILE_3 = [71,72,73,74,75,76,77,78]
FILE_2 = [81,82,83,84,85,86,87,88]
FILE_1 = [91,92,93,94,95,96,97,98]

class Board:
    start_board = np.array([[' ','n','b','q',' ',' ','r','r'],
                            ['p','p',' ',' ','n','p','p','p'],
                            [' ',' ',' ','p',' ',' ',' ',' '],
                            [' ',' ',' ','B','p',' ',' ',' '],
                            [' ',' ',' ',' ',' ',' ',' ','k'],
                            ['R',' ',' ',' ',' ',' ',' ',' '],
                            ['P','P','P','P','P','P','P','P'],
                            ['R','N',' ',' ',' ',' ','K',' ']])

    def __init__(self,board=start_board,WP=[],WN=[],WB=[],WR=[],WQ=[],WK=[],BP=[],BN=[],BB=[],BR=[],BQ=[],BK=[],ALL=[],W_ALL = [],B_ALL =[],
                 WSC=True,WLC=True,BSC=True,BLC=True,WK_moved = False,BK_moved = False,WSR_moved = False,WLR_moved=False,
                 BSR_moved = False,BLR_moved = False,WK_checked = False,BK_checked = False,W_PLmoves = [],B_PLmoves = [],W_Pmoves = [],B_Pmoves = []):
        self.board = board
        self.WP,self.WN, self.WB, self.WR, self.WQ, self.WK, self.BP, self.BN, self.BB, self.BR, self.BQ, self.BK = WP,WN,WB,WR,WQ,WK,BP,BN,BB,BR,BQ,BK
        self.ALL = ALL
        self.W_ALL = W_ALL
        self.B_ALL = B_ALL
        self.WSC = WSC
        self.WLC = WLC
        self.BSC = BSC
        self.BLC = BLC
        self.WK_moved = WK_moved
        self.BK_moved = BK_moved
        self.WSR_moved = WSR_moved
        self.WLR_moved = WLR_moved
        self.BSR_moved = BSR_moved
        self.BLR_moved = BLR_moved
        self.WK_checked = WK_checked
        self.BK_checked = BK_checked
        self.W_PLmoves = W_PLmoves
        self.B_PLmoves = B_PLmoves
        self.W_Pmoves = W_Pmoves
        self.B_Pmoves = B_Pmoves



    def arrayToBitBoards(self):
        bitBoardList = [[],[],[],[],[],[],[],[],[],[],[],[]]
        simbolList = ['P','N','B','R','Q','K','p','n','b','r','q','k']
        bits = []
        for boards,simbol in zip(bitBoardList,simbolList):
            for i in range(8):
                for j in range(8):
                    if self.board[i][j] == simbol:
                        boards.append(1)
                    else:
                        boards.append(0)
            bits.append(boards)
        bits = [np.asarray(bits[i]) for i in range(len(bits))]
        self.WP,self.WN, self.WB, self.WR, self.WQ, self.WK, self.BP, self.BN, self.BB, self.BR, self.BQ, self.BK = bits[0],bits[1],bits[2],bits[3],bits[4],bits[5],bits[6],bits[7],bits[8],bits[9],bits[10],bits[11]

        self.ALL = np.asarray(self.ALL)
        self.ALL = self.WP | self.WN | self.WB | self.WR | self.WQ | self.WK | self.BP | self.BN | self.BB | self.BR | self.BQ | self.BK

        self.W_ALL = np.asarray(self.W_ALL)
        self.W_ALL = self.WP | self.WN | self.WB | self.WR | self.WQ | self.WK

        self.B_ALL = np.asarray(self.B_ALL)
        self.B_ALL = self.BP | self.BN | self.BB | self.BR | self.BQ | self.BK

    def Display(self,map):
        for i in range(0,64,8):
            print(map[i:i+8])
            print()
        print(type(map))
        print(map.shape)


    def get_board_state(self):
        stateBoard = np.array([' ' for i in range(64)])
        for i in range(64):
            if self.BP[i] == 1:
                stateBoard[i] = 'p'
            if self.BN[i] == 1:
                stateBoard[i] = 'n'
            if self.BB[i] == 1:
                stateBoard[i] = 'b'
            if self.BR[i] == 1:
                stateBoard[i] = 'r'
            if self.BQ[i] == 1:
                stateBoard[i] = 'q'
            if self.BK[i] == 1:
                stateBoard[i] = 'k'
            if self.WP[i] == 1:
                stateBoard[i] = 'P'
            if self.WN[i] == 1:
                stateBoard[i] = 'N'
            if self.WB[i] == 1:
                stateBoard[i] = 'B'
            if self.WR[i] == 1:
                stateBoard[i] = 'R'
            if self.WQ[i] == 1:
                stateBoard[i] = 'Q'
            if self.WK[i] == 1:
                stateBoard[i] = 'K'
        self.board = stateBoard
        return self.board

    def drawBoard(self):
        print(self.board)



b = Board()
b.arrayToBitBoards()





