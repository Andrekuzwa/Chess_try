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

# state_board = np.array(['r', ' ', ' ', ' ', ' ', ' ', ' ', 'r',
#                         ' ', ' ', 'p', ' ', 'k', 'p', ' ', 'N',
#                         ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ',
#                         'p', ' ', ' ', 'p', ' ', ' ', ' ', ' ',
#                         'P', 'p', ' ', 'P', ' ', ' ', ' ', ' ',
#                         'K', 'P', ' ', 'B', 'P', ' ', 'P', ' ',
#                         ' ', ' ', ' ', ' ', ' ', 'P', ' ', 'P',
#                         ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'R'])


RANK_8 = [21,22,23,24,25,26,27,28]
RANK_7 = [31,32,33,34,35,36,37,38]
RANK_6 = [41,42,43,44,45,46,47,48]
RANK_5 = [51,52,53,54,55,56,57,58]
RANK_4 = [61,62,63,64,65,66,67,68]
RANK_3 = [71,72,73,74,75,76,77,78]
RANK_2 = [81,82,83,84,85,86,87,88]
RANK_1 = [91,92,93,94,95,96,97,98]


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

# state_board = np.array(['r','n','b','q','k','b','n','r',
#                             'p','p','p','p','p','p','p','p',
#                             ' ',' ',' ',' ',' ',' ',' ',' ',
#                             ' ',' ',' ',' ',' ',' ',' ',' ',
#                             ' ',' ',' ',' ',' ',' ',' ',' ',
#                             ' ',' ',' ',' ',' ',' ',' ',' ',
#                             'P','P','P','P','P','P','P','P',
#                             'R','N','B','Q','K','B','N','R'])

# state_board = np.array([' ',' ',' ',' ','k',' ',' ',' ',
#                             ' ',' ',' ',' ',' ',' ',' ',' ',
#                             ' ',' ',' ',' ',' ',' ',' ',' ',
#                             ' ',' ',' ',' ',' ',' ',' ',' ',
#                             ' ',' ',' ',' ',' ',' ',' ',' ',
#                             ' ',' ',' ',' ',' ',' ',' ',' ',
#                             ' ',' ',' ',' ',' ',' ',' ',' ',
#                             ' ',' ',' ',' ','K',' ',' ',' '])

class Board:
    state_board = np.array(['r', ' ', ' ', ' ', ' ', ' ', ' ', 'r',
                            ' ', ' ', 'p', ' ', 'k', 'p', ' ', 'N',
                            ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ',
                            'p', ' ', ' ', 'p', ' ', ' ', ' ', ' ',
                            'P', 'p', ' ', 'P', ' ', ' ', ' ', ' ',
                            'K', 'P', ' ', 'B', 'P', ' ', 'P', ' ',
                            ' ', ' ', ' ', ' ', ' ', 'P', ' ', 'P',
                            ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'R'])

    def __init__(self,board=state_board,WP=[],WN=[],WB=[],WR=[],WQ=[],WK=[],BP=[],BN=[],BB=[],BR=[],BQ=[],BK=[],ALL=[],W_ALL = [],B_ALL =[],
                 WSC=True,WLC=True,BSC=True,BLC=True,WK_moved = False,BK_moved = False,WSR_moved = False,WLR_moved=False,
                 BSR_moved = False,BLR_moved = False,WK_checked = False,BK_checked = False,W_PLPmoves = [],B_PLPmoves = [],W_PLmoves = [],B_PLmoves = [],W_Lmoves = [],B_Lmoves = [],
                 whitePawnAttMap = [],blackPawnAttMap = [],PLmoves_whitePawn = [],PLmoves_blackPawn = [],
                 whiteNightAttMap=[], blackNightAttMap=[], PLmoves_whiteNight=[], PLmoves_blackNight=[],
                 whiteBishopAttMap = [],blackBishopAttMap = [],PLmoves_whiteBishop = [],PLmoves_blackBishop = [],
                 whiteRookAttMap = [],blackRookAttMap = [],PLmoves_whiteRook = [],PLmoves_blackRook = [],
                 whiteQueenAttMap = [],blackQueenAttMap = [],PLmoves_whiteQueen = [],PLmoves_blackQueen = [],
                 whiteKingAttMap = [],blackKingAttMap = [],PLmoves_whiteKing = [],PLmoves_blackKing = [],
                 matedWhite = False,matedBlack = False,draw = False,evaluation = 0):

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

        self.W_Lmoves = W_Lmoves
        self.B_Lmoves = B_Lmoves

        self.matedWhite = matedWhite
        self.matedBlack = matedBlack
        self.draw = draw
        self.evaluation = evaluation
        

        self.arrayToBitBoards()
        self.whitePawnAttMap = self.whitePawnAttMapDef()
        self.blackPawnAttMap = self.blackPawnAttMapDef()
        self.PLmoves_whitePawn = self.PLmoves_whitePawnDef()
        self.PLmoves_blackPawn = self.PLmoves_blackPawnDef()
        self.whiteNightAttMap = self.whiteNightAttMapDef()
        self.blackNightAttMap = self.blackNightAttMapDef()
        self.PLmoves_whiteNight = self.PLmoves_whiteNightDef()
        self.PLmoves_blackNight = self.PLmoves_blackNightDef()
        self.whiteBishopAttMap = self.whiteBishopAttMapDef()
        self.blackBishopAttMap = self.blackBishopAttMapDef()
        self.PLmoves_whiteBishop = self.PLmoves_whiteBishopDef()
        self.PLmoves_blackBishop = self.PLmoves_blackBishopDef()
        self.whiteRookAttMap = self.whiteRookAttMapDef()
        self.blackRookAttMap = self.blackRookAttMapDef()
        self.PLmoves_whiteRook = self.PLmoves_whiteRookDef()
        self.PLmoves_blackRook = self.PLmoves_blackRookDef()
        self.whiteQueenAttMap = self.whiteQueenAttMapDef()
        self.blackQueenAttMap = self.blackQueenAttMapDef()
        self.PLmoves_whiteQueen = self.PLmoves_whiteQueenDef()
        self.PLmoves_blackQueen = self.PLmoves_blackQueenDef()
        self.whiteKingAttMap = self.whiteKingAttMaDef()
        self.blackKingAttMap = self.blackKingAttMapDef()
        self.PLmoves_whiteKing = self.PLmoves_whiteKingDef()
        self.PLmoves_blackKing = self.PLmoves_blackKingDef()
        self.W_PLPmoves = self.PLmoves_whiteNight + self.PLmoves_whiteBishop + self.PLmoves_whiteRook + self.PLmoves_whiteQueen + self.PLmoves_whiteKing
        self.B_PLPmoves = self.PLmoves_blackNight + self.PLmoves_blackBishop + self.PLmoves_blackRook + self.PLmoves_blackQueen + self.PLmoves_blackKing
        self.W_PLmoves = self.PLmoves_whitePawn + self.PLmoves_whiteNight + self.PLmoves_whiteBishop + self.PLmoves_whiteRook + self.PLmoves_whiteQueen + self.PLmoves_whiteKing
        self.B_PLmoves = self.PLmoves_blackPawn + self.PLmoves_blackNight + self.PLmoves_blackBishop + self.PLmoves_blackRook + self.PLmoves_blackQueen + self.PLmoves_blackKing
        self.whiteCheckUpdate()
        self.blackCheckUpdate()
        self.Lmoves_whiteDef()
        self.Lmoves_blackDef()
        self.mateDrawCheck()


    def arrayToBitBoards(self):
        bitBoardList = [[],[],[],[],[],[],[],[],[],[],[],[]]
        simbolList = ['P','N','B','R','Q','K','p','n','b','r','q','k']
        bits = []
        for boards,simbol in zip(bitBoardList,simbolList):
            for i in range(64):
                if self.board[i] == simbol:
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

    def Display(self):
        ranks = [8,7,6,5,4,3,2,1]
        files = ['a','b','c','d','e','f','g','h']
        board8x8 = np.reshape(self.board,(8,8))
        for i in range(8):
            print(str(ranks[i]) + ' |',end='')
            for j in range(8):
                print(board8x8[i][j]+'|',end='')
            print()
        print('   a b c d e f g h')

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

    def moveMaker(self,a,b):
        board120 = array64_to_array120(self.board)
        board120[b] = board120[a]
        board120[a] = ' '
        board64 = array120_to_array64(board120)
        self.board = board64

    def whitePawnAttMapDef(self):
        board120 = array64_to_array120(self.WP)
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
        board120 = array64_to_array120(self.WP)
        blackPieces120 = array64_to_array120(self.B_ALL)
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
                if i in RANK_2 and (blackPieces120 | whitePieces120)[i-10]==0 and (blackPieces120 | whitePieces120)[i-20]==0 and  i-20 in in_index:
                    move_list.append((i,i-20))
        return move_list

    def PLmoves_blackPawnDef(self):
        board120 = array64_to_array120(self.BP)
        blackPieces120 = array64_to_array120(self.B_ALL)
        whitePieces120 = array64_to_array120(self.W_ALL)
        move_list = []
        for i in range(120):
            if board120[i] == 1:
                if whitePieces120[i + 11] == 1 and i + 11 in in_index:
                    move_list.append((i, i + 11))
                if whitePieces120[i + 9] == 1 and i + 9 in in_index:
                    move_list.append((i, i + 9))
                if (blackPieces120 | whitePieces120)[i + 10] == 0 and i + 10 in in_index:
                    move_list.append((i, i + 10))
                if i in RANK_7 and (blackPieces120 | whitePieces120)[i+10]==0 and (blackPieces120 | whitePieces120)[i+20]==0and  i+20 in in_index:
                    move_list.append((i, i + 20))
        return move_list

    def enPassantMove(self,a,b):
        board120 = array64_to_array120(self.board)
        if a-b == 11:
            board120[b] = board120[a]
            board120[a] = ' '
            board120[a-1] = ' '
        elif a-b == 9:
            board120[b] = board120[a]
            board120[a] = ' '
            board120[a + 1] = ' '
        elif a-b == -9:
            board120[b] = board120[a]
            board120[a] = ' '
            board120[a - 1] = ' '
        elif a-b == -11:
            board120[b] = board120[a]
            board120[a] = ' '
            board120[a + 1] = ' '
        board64 = array120_to_array64(board120)
        self.board = board64

    def whiteNightAttMapDef(self):
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

    def blackNightAttMapDef(self):
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

    def PLmoves_whiteNightDef(self):
        board120 = array64_to_array120(self.WN)
        blackPieces120 = array64_to_array120(self.B_ALL)
        whitePieces120 = array64_to_array120(self.W_ALL)
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
        board120 = array64_to_array120(self.BN)
        blackPieces120 = array64_to_array120(self.B_ALL)
        whitePieces120 = array64_to_array120(self.W_ALL)
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

    def whiteBishopAttMapDef(self):
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

    def blackBishopAttMapDef(self):
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

    def PLmoves_whiteBishopDef(self):
        board120 = array64_to_array120(self.WB)
        blackPieces120 = array64_to_array120(self.B_ALL)
        whitePieces120 = array64_to_array120(self.W_ALL)
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
        board120 = array64_to_array120(self.BB)
        blackPieces120 = array64_to_array120(self.B_ALL)
        whitePieces120 = array64_to_array120(self.W_ALL)
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

    def whiteRookAttMapDef(self):
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

    def blackRookAttMapDef(self):
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

    def PLmoves_whiteRookDef(self):
        board120 = array64_to_array120(self.WR)
        blackPieces120 = array64_to_array120(self.B_ALL)
        whitePieces120 = array64_to_array120(self.W_ALL)
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
        board120 = array64_to_array120(self.BR)
        blackPieces120 = array64_to_array120(self.B_ALL)
        whitePieces120 = array64_to_array120(self.W_ALL)
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

    def whiteQueenAttMapDef(self):
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

    def blackQueenAttMapDef(self):
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

    def PLmoves_whiteQueenDef(self):
        board120 = array64_to_array120(self.WQ)
        blackPieces120 = array64_to_array120(self.B_ALL)
        whitePieces120 = array64_to_array120(self.W_ALL)
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
        board120 = array64_to_array120(self.BQ)
        blackPieces120 = array64_to_array120(self.B_ALL)
        whitePieces120 = array64_to_array120(self.W_ALL)
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

    def whiteKingAttMaDef(self):
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

    def blackKingAttMapDef(self):
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

    def PLmoves_whiteKingDef(self):
        board120 = array64_to_array120(self.WK)
        blackPieces120 = array64_to_array120(self.B_ALL)
        whitePieces120 = array64_to_array120(self.W_ALL)
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
                if blackPieces120[i + 11] == 1 or whitePieces120[i + 11] == 0 and i + 11 in in_index:
                    move_list.append((i, i + 11))
        return move_list

    def PLmoves_blackKingDef(self):
        board120 = array64_to_array120(self.BK)
        blackPieces120 = array64_to_array120(self.B_ALL)
        whitePieces120 = array64_to_array120(self.W_ALL)
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
        if self.WK_moved == True:
            self.WSC = False
            self.WLC = False
        if self.WSR_moved == True:
            self.WSC = False
        if self.WLR_moved == True:
            self.WLC = False
        if self.ALL[61] == 0 and self.ALL[62] == 0 and\
                (96 not in [item[1] for item in self.B_PLPmoves]) and\
                (97 not in [item[1] for item in self.B_PLPmoves]) and\
                self.blackPawnAttMap[61] == 0 and\
                self.blackPawnAttMap[62] == 0 and\
                self.WK_checked == False:
            moves.append((95,97))
        if self.ALL[57] == 0 and self.ALL[58] == 0 and self.ALL[59] == 0 and\
                (92 not in [item[1] for item in self.B_PLPmoves]) and\
                (93 not in [item[1] for item in self.B_PLPmoves]) and\
                (94 not in [item[1] for item in self.B_PLPmoves]) and\
                self.blackPawnAttMap[57] == 0 and\
                self.blackPawnAttMap[58] == 0 and\
                self.blackPawnAttMap[59] == 0 and\
                self.WK_checked == False:
            moves.append((95,93))
        return moves

    def blackCastleCheck(self):
        moves = []
        if self.BK_moved == True:
            self.BSC = False
            self.BLC = False
        if self.BSR_moved == True:
            self.BSC = False
        if self.BLR_moved == True:
            self.BLC = False
        if self.ALL[5] == 0 and self.ALL[6] == 0 and\
                (26 not in [item[1] for item in self.W_PLPmoves]) and\
                (27 not in [item[1] for item in self.W_PLPmoves]) and\
                self.whitePawnAttMap[5] == 0 and\
                self.whitePawnAttMap[6] == 0 and\
                self.BK_checked == False:
            moves.append((25,27))
        if self.ALL[1] == 0 and self.ALL[2] == 0 and self.ALL[3] == 0 and\
                (22 not in [item[1] for item in self.W_PLPmoves]) and\
                (23 not in [item[1] for item in self.W_PLPmoves]) and\
                (24 not in [item[1] for item in self.W_PLPmoves]) and\
                self.whitePawnAttMap[1] == 0 and\
                self.whitePawnAttMap[2] == 0 and\
                self.whitePawnAttMap[3] == 0 and\
                self.BK_checked == False:
            moves.append((25,23))
        return moves

    def whiteCheckUpdate(self):
        board120 = array64_to_array120(self.WK)
        for i in range(120):
            if board120[i] == 1:
                if i in [item[1] for item in self.B_PLPmoves] or True in self.blackPawnAttMap & self.WK:
                    self.WK_checked = True
                else:
                    self.WK_checked = False

    def blackCheckUpdate(self):
        board120 = array64_to_array120(self.BK)
        for i in range(120):
            if board120[i] == 1:
                if i in [item[1] for item in self.W_PLPmoves] or True in self.whitePawnAttMap & self.BK:
                    self.BK_checked = True
                else:
                    self.BK_checked = False

    def updateMaps(self):
        self.arrayToBitBoards()
        self.whitePawnAttMap = self.whitePawnAttMapDef()
        self.blackPawnAttMap = self.blackPawnAttMapDef()
        self.PLmoves_whitePawn = self.PLmoves_whitePawnDef()
        self.PLmoves_blackPawn = self.PLmoves_blackPawnDef()
        self.whiteNightAttMap = self.whiteNightAttMapDef()
        self.blackNightAttMap = self.blackNightAttMapDef()
        self.PLmoves_whiteNight = self.PLmoves_whiteNightDef()
        self.PLmoves_blackNight = self.PLmoves_blackNightDef()
        self.whiteBishopAttMap = self.whiteBishopAttMapDef()
        self.blackBishopAttMap = self.blackBishopAttMapDef()
        self.PLmoves_whiteBishop = self.PLmoves_whiteBishopDef()
        self.PLmoves_blackBishop = self.PLmoves_blackBishopDef()
        self.whiteRookAttMap = self.whiteRookAttMapDef()
        self.blackRookAttMap = self.blackRookAttMapDef()
        self.PLmoves_whiteRook = self.PLmoves_whiteRookDef()
        self.PLmoves_blackRook = self.PLmoves_blackRookDef()
        self.whiteQueenAttMap = self.whiteQueenAttMapDef()
        self.blackQueenAttMap = self.blackQueenAttMapDef()
        self.PLmoves_whiteQueen = self.PLmoves_whiteQueenDef()
        self.PLmoves_blackQueen = self.PLmoves_blackQueenDef()
        self.whiteKingAttMap = self.whiteKingAttMaDef()
        self.blackKingAttMap = self.blackKingAttMapDef()
        self.PLmoves_whiteKing = self.PLmoves_whiteKingDef()
        self.PLmoves_blackKing = self.PLmoves_blackKingDef()
        self.W_PLPmoves = self.PLmoves_whiteNight + self.PLmoves_whiteBishop + self.PLmoves_whiteRook + self.PLmoves_whiteQueen + self.PLmoves_whiteKing
        self.B_PLPmoves = self.PLmoves_blackNight + self.PLmoves_blackBishop + self.PLmoves_blackRook + self.PLmoves_blackQueen + self.PLmoves_blackKing
        self.W_PLmoves = self.PLmoves_whitePawn + self.PLmoves_whiteNight + self.PLmoves_whiteBishop + self.PLmoves_whiteRook + self.PLmoves_whiteQueen + self.PLmoves_whiteKing
        self.B_PLmoves = self.PLmoves_blackPawn + self.PLmoves_blackNight + self.PLmoves_blackBishop + self.PLmoves_blackRook + self.PLmoves_blackQueen + self.PLmoves_blackKing
        self.whiteCheckUpdate()
        self.blackCheckUpdate()

    def Lmoves_whiteDef(self):
        self.W_Lmoves = []
        start_state = self.board
        for move in self.W_PLmoves:
            self.moveMaker(move[0],move[1])
            self.updateMaps()
            if self.WK_checked == False:
                self.W_Lmoves.append(move)
            self.board = start_state
            self.updateMaps()
        for item in self.whiteCastleCheck():
            self.W_Lmoves.append(item)

    def Lmoves_blackDef(self):
        self.B_Lmoves = []
        start_state = self.board
        for move in self.B_PLmoves:
            self.moveMaker(move[0], move[1])
            self.updateMaps()
            if self.BK_checked == False:
                self.B_Lmoves.append(move)
            self.board = start_state
            self.updateMaps()
        for item in self.blackCastleCheck():
            self.B_Lmoves.append(item)

    def castleWSC(self):
        if self.WSC == True:
            self.board[60] = ' '
            self.board[63] = ' '
            self.board[62] = 'K'
            self.board[61] = 'R'
            self.updateMaps()

    def castleWLC(self):
        if self.WLC == True:
            self.board[60] = ' '
            self.board[56] = ' '
            self.board[58] = 'K'
            self.board[59] = 'R'
            self.updateMaps()

    def castleBSC(self):
        if self.BSC == True:
            self.board[4] = ' '
            self.board[7] = ' '
            self.board[6] = 'k'
            self.board[5] = 'r'
            self.updateMaps()

    def castleBLC(self):
        if self.BLC == True:
            self.board[4] = ' '
            self.board[0] = ' '
            self.board[2] = 'k'
            self.board[3] = 'r'
            self.updateMaps()

    def whitePromotion(self):
        board120 = array64_to_array120(self.board)
        board120P = array64_to_array120(self.WP)
        for i in range(120):
            if board120P[i] == 1:
                if i in RANK_8:
                    choice = input("Choose:\nQ - Queen\nR-Rook\nB-Bishop\nN-Knight")
                    if choice.upper() == 'Q':
                        board120[i] = 'Q'
                        self.board = array120_to_array64(board120)
                    elif choice.upper() == 'R':
                        board120[i] = 'R'
                        self.board = array120_to_array64(board120)
                    elif choice.upper() == 'B':
                        board120[i] = 'B'
                        self.board = array120_to_array64(board120)
                    elif choice.upper() == 'N':
                        board120[i] = 'B'
                        self.board = array120_to_array64(board120)
                    else:
                        print('No option',choice)

    def blackPromotion(self):
        board120 = array64_to_array120(self.board)
        board120P = array64_to_array120(self.BP)
        for i in range(120):
            if board120P[i] == 1:
                if i in RANK_1:
                    choice = input("Choose:\nQ - Queen\nR-Rook\nB-Bishop\nN-Knight")
                    if choice.upper() == 'Q':
                        board120[i] = 'q'
                        self.board = array120_to_array64(board120)
                    elif choice.upper() == 'R':
                        board120[i] = 'r'
                        self.board = array120_to_array64(board120)
                    elif choice.upper() == 'B':
                        board120[i] = 'b'
                        self.board = array120_to_array64(board120)
                    elif choice.upper() == 'N':
                        board120[i] = 'n'
                        self.board = array120_to_array64(board120)
                    else:
                        print('No option', choice)

    def mateDrawCheck(self):
        if len(self.W_Lmoves) == 0 and self.WK_checked == True:
            self.matedWhite = True
        elif len(self.W_Lmoves) == 0 and self.WK_checked == False:
            self.draw = True

        if len(self.B_Lmoves) == 0 and self.BK_checked == True:
            self.matedBlack = True
        elif len(self.B_Lmoves) == 0 and self.BK_checked == False:
            self.draw = True

        if False not in (self.WK | self.BK == self.ALL):
            self.draw = True
        elif False not in (self.WK | self.WN | self.BK == self.ALL) and np.sum(self.WN == 1) == 1:
            self.draw = True
        elif False not in (self.BK | self.BN | self.WK == self.ALL) and np.sum(self.BN == 1) == 1:
            self.draw = True
        elif False not in (self.WK | self.WB | self.BK == self.ALL) and np.sum(self.WB == 1) == 1:
            self.draw = True
        elif False not in (self.BK | self.BB | self.WK == self.ALL) and np.sum(self.BB == 1) == 1:
            self.draw = True

    def evaluate(self):
        W_value = 0
        B_value = 0
        for i,j in zip(self.WP,self.BP):
            if i == 1:
                W_value+=10
            if j == 1:
                B_value+=10
        for i,j in zip(self.WN,self.BN):
            if i == 1:
                W_value+=30
            if j == 1:
                B_value+=30
        for i,j in zip(self.WB,self.BB):
            if i == 1:
                W_value+=35
            if j == 1:
                B_value+=35
        for i,j in zip(self.WR,self.BR):
            if i == 1:
                W_value+=50
            if j == 1:
                B_value+=50
        for i,j in zip(self.WQ,self.BQ):
            if i == 1:
                W_value+=90
            if j == 1:
                B_value+=90
        for i,j in zip(self.WK,self.BK):
            if i == 1:
                W_value+=9000
            if j == 1:
                B_value+=9000
        self.evaluation = W_value - B_value







        pass







