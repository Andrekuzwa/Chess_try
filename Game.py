import numpy as np
import copy
from BoardClass import Board
import time
import chess
import chess.polyglot

short = {'a8':21,'b8':22,'c8':23,'d8':24,'e8':25,'f8':26,'g8':27,'h8':28,
         'a7':31,'b7':32,'c7':33,'d7':34,'e7':35,'f7':36,'g7':37,'h7':38,
         'a6':41,'b6':42,'c6':43,'d6':44,'e6':45,'f6':46,'g6':47,'h6':48,
         'a5':51,'b5':52,'c5':53,'d5':54,'e5':55,'f5':56,'g5':57,'h5':58,
         'a4':61,'b4':62,'c4':63,'d4':64,'e4':65,'f4':66,'g4':67,'h4':68,
         'a3':71,'b3':72,'c3':73,'d3':74,'e3':75,'f3':76,'g3':77,'h3':78,
         'a2':81,'b2':82,'c2':83,'d2':84,'e2':85,'f2':86,'g2':87,'h2':88,
         'a1':91,'b1':92,'c1':93,'d1':94,'e1':95,'f1':96,'g1':97,'h1':98}

long = dict(zip(short.values(),short.keys()))


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

nodes = 0
class Game:
    def __init__(self,OB,playerStarts,ruch=1,moveHist = [],draw = False,enPassantMoves = [],boardStateList=[],evaluation = 0,end_game=False):
        self.OB = OB
        self.ruch = ruch
        self.moveHist = moveHist
        self.draw = draw
        self.enPassantMoves = enPassantMoves
        self.boardStateList = boardStateList
        self.playerStarts = playerStarts
        self.evaluation = evaluation
        self.end_game = end_game
        self.OB.updateMaps()

    def start_game_1vs1(self):
        self.OB.Display()
        while self.OB.matedWhite == False and self.OB.matedBlack == False and self.OB.draw == False:
            if self.ruch == 1:
                self.enPassantLegalMovesDef()
                if self.repetitionDraw() == True:
                    break
                print("Whites turn")
                print("Wykonaj ruch używając notacji - np. e2 -> enter -> e4")
                x = input().lower()
                if x not in short:
                    print("Incorrect input")
                elif short[x] not in [item[0] for item in self.OB.W_Lmoves] and short[x] not in [item[0] for item in self.enPassantMoves]:
                    print('No legal moves for this position')
                else:
                    print([long[item[1]] for item in self.OB.W_Lmoves if item[0] == short[x]] + [long[item[1]] for item in self.enPassantMoves if item[0] == short[x]])
                    y = input().lower()
                    if y not in short:
                        print("Incorrect input")
                    elif short[y] not in [item[1] for item in self.OB.W_Lmoves if item[0] == short[x]] and short[y] not in [item[1] for item in self.enPassantMoves if item[0] == short[x]]:
                        print('Illegal move')
                    else:
                        self.makeGameMove(short[x],short[y])

            else:
                self.enPassantLegalMovesDef()
                if self.repetitionDraw() == True:
                    break
                print("Blacks turn")
                print("Wykonaj ruch używając notacji - np. e2 -> enter -> e4")
                x = input().lower()
                if x not in short:
                    print("Incorrect input")
                elif short[x] not in [item[0] for item in self.OB.B_Lmoves] and  short[x] not in [item[0] for item in self.enPassantMoves]:
                    print('No legal moves for this position')
                else:
                    print([long[item[1]] for item in self.OB.B_Lmoves if item[0] == short[x]] + [long[item[1]] for item in self.enPassantMoves if item[0] == short[x]])
                    y = input().lower()
                    if y not in short:
                        print("Incorrect input")
                    elif short[y] not in [item[1] for item in self.OB.B_Lmoves if item[0] == short[x]] and short[y] not in [item[1] for item in self.enPassantMoves if item[0] == short[x]]:
                        print('Illegal move')
                    else:
                        self.makeGameMove(short[x],short[y])



        if self.OB.matedWhite == True:
            print('BLACK WINS')
        elif self.OB.matedBlack == True:
            print("WHITE WINS")
        elif self.OB.draw == True:
            print('DRAW')

    def evaluate(self):
        W_value = 0
        B_value = 0
        W_material = 0
        B_material = 0

        pawn_map = [0, 0, 0, 0, 0, 0, 0, 0,
                    50, 50, 50, 50, 50, 50, 50, 50,
                    10, 10, 20, 30, 30, 20, 10, 10,
                    5, 5, 10, 25, 25, 10, 5, 5,
                    0, 0, 0, 20, 20, 0, 0, 0,
                    5, -5, -10, 0, 0, -10, -5, 5,
                    5, 10, 10, -20, -20, 10, 10, 5,
                    0, 0, 0, 0, 0, 0, 0, 0]
        night_map = [-50, -40, -30, -30, -30, -30, -40, -50,
                     -40, -20, 0, 0, 0, 0, -20, -40,
                     -30, 0, 10, 15, 15, 10, 0, -30,
                     -30, 5, 15, 20, 20, 15, 5, -30,
                     -30, 0, 15, 20, 20, 15, 0, -30,
                     -30, 5, 10, 15, 15, 10, 5, -30,
                     -40, -20, 0, 5, 5, 0, -20, -40,
                     -50, -40, -30, -30, -30, -30, -40, -50]
        bishop_map = [-20, -10, -10, -10, -10, -10, -10, -20,
                      -10, 0, 0, 0, 0, 0, 0, -10,
                      -10, 0, 5, 10, 10, 5, 0, -10,
                      -10, 5, 5, 10, 10, 5, 5, -10,
                      -10, 0, 10, 10, 10, 10, 0, -10,
                      -10, 10, 10, 10, 10, 10, 10, -10,
                      -10, 5, 0, 0, 0, 0, 5, -10,
                      -20, -10, -10, -10, -10, -10, -10, -20]
        rook_map = [0, 0, 0, 0, 0, 0, 0, 0,
                    5, 10, 10, 10, 10, 10, 10, 5,
                    -5, 0, 0, 0, 0, 0, 0, -5,
                    -5, 0, 0, 0, 0, 0, 0, -5,
                    -5, 0, 0, 0, 0, 0, 0, -5,
                    -5, 0, 0, 0, 0, 0, 0, -5,
                    -5, 0, 0, 0, 0, 0, 0, -5,
                    0, 0, 0, 5, 5, 0, 0, 0]
        queen_map = [-20, -10, -10, -5, -5, -10, -10, -20,
                     -10, 0, 0, 0, 0, 0, 0, -10,
                     -10, 0, 5, 5, 5, 5, 0, -10,
                     -5, 0, 5, 5, 5, 5, 0, -5,
                     0, 0, 5, 5, 5, 5, 0, -5,
                     -10, 5, 5, 5, 5, 5, 0, -10,
                     -10, 0, 5, 0, 0, 0, 0, -10,
                     -20, -10, -10, -5, -5, -10, -10, -20]

        for i in range(64):
            if self.OB.WP[i] == 1:
                W_value += 100
                W_material+= 1
            if self.OB.BP[i] == 1:
                B_value += 100
                B_material+=1

            if self.OB.WN[i] == 1:
                W_value += 320
                W_material += 3
            if self.OB.BN[i] == 1:
                B_value += 320
                B_material += 3

            if self.OB.WB[i] == 1:
                W_value += 330
                W_material += 3
            if self.OB.BB[i] == 1:
                B_value += 330
                B_material += 3

            if self.OB.WR[i] == 1:
                W_value += 500
                W_material += 5
            if self.OB.BR[i] == 1:
                B_value += 500
                B_material += 5

            if self.OB.WQ[i] == 1:
                W_value += 900
                W_material += 9
            if self.OB.BQ[i] == 1:
                B_value += 900
                B_material += 9

            king_map = [-30,-40,-40,-50,-50,-40,-40,-30,
                        -30,-40,-40,-50,-50,-40,-40,-30,
                        -30,-40,-40,-50,-50,-40,-40,-30,
                        -30,-40,-40,-50,-50,-40,-40,-30,
                        -20,-30,-30,-40,-40,-30,-30,-20,
                        -10,-20,-20,-20,-20,-20,-20,-10,
                         20, 20,  0,  0,  0,  0, 20, 20,
                         20, 30, 10,  0,  0, 10, 30, 20]

            if W_material <= 13 and B_material <= 13:
                self.end_game = True
                king_map = [-50,-40,-30,-20,-20,-30,-40,-50,
                            -30,-20,-10,  0,  0,-10,-20,-30,
                            -30,-10, 20, 30, 30, 20,-10,-30,
                            -30,-10, 30, 40, 40, 30,-10,-30,
                            -30,-10, 30, 40, 40, 30,-10,-30,
                            -30,-10, 20, 30, 30, 20,-10,-30,
                            -30,-30,  0,  0,  0,  0,-30,-30,
                            -50,-30,-30,-30,-30,-30,-30,-50]

            if self.OB.WK[i] == 1:
                W_value += 20000
            if self.OB.BK[i] == 1:
                B_value += 20000


            W_value += self.OB.WP[i] * pawn_map[i]
            B_value += self.OB.BP[i] * pawn_map[63 - i]
            W_value += self.OB.WN[i] * night_map[i]
            B_value += self.OB.BN[i] * night_map[63 - i]
            W_value += self.OB.WB[i] * bishop_map[i]
            B_value += self.OB.BB[i] * bishop_map[63 - i]
            W_value += self.OB.WR[i] * rook_map[i]
            B_value += self.OB.BR[i] * rook_map[63 - i]
            W_value += self.OB.WQ[i] * queen_map[i]
            B_value += self.OB.BQ[i] * queen_map[63 - i]
            W_value += self.OB.WK[i] * king_map[i]
            B_value += self.OB.BK[i] * king_map[63 - i]

        self.evaluation = W_value - B_value

    def makeGameMove(self,x,y):
        if (x, y) in self.enPassantMoves:
            self.OB.enPassantMove(x, y)
        elif x == 25 and y == 27:
            self.OB.castleBSC()
        elif x == 25 and y == 23:
            self.OB.castleBLC()
        elif x == 95 and y == 97:
            self.OB.castleWSC()
        elif x == 95 and y == 93:
            self.OB.castleWLC()
        else:
            self.OB.moveMaker(x, y)
        self.kingsRooksMovedCheck(x)
        self.OB.updateMaps()
        self.OB.blackPromotion(self.playerStarts)
        self.OB.whitePromotion(self.playerStarts)
        self.OB.updateMaps()
        self.OB.Lmoves_whiteDef()
        self.OB.Lmoves_blackDef()
        self.OB.mateDrawCheck()
        self.moveHist.append((x, y))
        if self.ruch == 1:
            self.ruch = 0
        else:
            self.ruch = 1

    def enPassantLegalMovesDef(self):
        self.enPassantMoves = []
        start_state = self.OB.board
        board120WP = array64_to_array120(self.OB.WP)
        board120BP = array64_to_array120(self.OB.BP)
        moves = []
        if self.ruch == 1:
            if len(self.moveHist) > 0:
                if self.moveHist[-1][0] in RANK_7 and (self.moveHist[-1][1] - self.moveHist[-1][0] == 20) and \
                        board120BP[self.moveHist[-1][1]] == 1:
                    if board120WP[self.moveHist[-1][1] + 1] == 1:
                        moves.append((self.moveHist[-1][1] + 1, self.moveHist[-1][1] - 10))
                    if board120WP[self.moveHist[-1][1] - 1] == 1:
                        moves.append((self.moveHist[-1][1] - 1, self.moveHist[-1][1] - 10))
            if len(moves)>0:
                for move in moves:
                    self.OB.enPassantMove(move[0],move[1])
                    self.OB.updateMaps()
                    if self.OB.WK_checked == False:
                        self.enPassantMoves.append(move)
                    self.OB.board = start_state
                    self.OB.updateMaps()

        if self.ruch == 0:
            if len(self.moveHist) > 0:
                if self.moveHist[-1][0] in RANK_2 and (self.moveHist[-1][1] - self.moveHist[-1][0] == -20) and \
                        board120WP[self.moveHist[-1][1]] == 1:
                    if board120BP[self.moveHist[-1][1] + 1] == 1:
                        moves.append((self.moveHist[-1][1] + 1, self.moveHist[-1][1] + 10))
                    if board120BP[self.moveHist[-1][1] - 1] == 1:
                        moves.append((self.moveHist[-1][1] - 1, self.moveHist[-1][1] + 10))
            if len(moves)>0:
                for move in moves:
                    self.OB.enPassantMove(move[0], move[1])
                    self.OB.updateMaps()
                    if self.OB.BK_checked == False:
                        self.enPassantMoves.append(move)
                    self.OB.board = start_state
                    self.OB.updateMaps()

    def repetitionDraw(self):
        self.boardStateList.append(
            [list(self.OB.board), self.OB.W_Lmoves, self.OB.B_Lmoves, self.enPassantMoves, self.OB.castleWSC,
             self.OB.castleWLC, self.OB.castleBSC, self.OB.castleBLC])
        if self.boardStateList.count(
                [list(self.OB.board), self.OB.W_Lmoves, self.OB.B_Lmoves, self.enPassantMoves, self.OB.castleWSC,
                 self.OB.castleWLC, self.OB.castleBSC, self.OB.castleBLC]) == 3:
            self.OB.draw = True
            return True

    def kingsRooksMovedCheck(self,a):
        if a == 21:
            self.BSR_moved = True
        elif a == 28:
            self.BLR_moved = True
        elif a == 25:
            self.BK_moved = True
        elif a == 91:
            self.WLR_moved = True
        elif a == 98:
            self.WSR_moved = True
        elif a == 95:
            self.WK_moved = True

class Game_vs_AI:
    def __init__(self,OB,playerStarts,depth,ruch=1,moveHist = [],draw = False,enPassantMoves = [],boardStateList=[]):
        self.OB = OB
        self.ruch = ruch
        self.moveHist = moveHist
        self.draw = draw
        self.playerStarts = playerStarts
        self.enPassantMoves = enPassantMoves
        self.boardStateList = boardStateList
        self.depth = depth
        self.OB.updateMaps()

    def start_game_vs_AI(self):
        pyBoard = chess.Board()
        game = Game(Board(),self.playerStarts)
        self.OB.Display()
        while self.OB.matedWhite == False and self.OB.matedBlack == False and self.OB.draw == False:
            if self.playerStarts == True:
                if self.ruch == 1:
                    self.enPassantLegalMovesDef()
                    if self.repetitionDraw() == True:
                        break
                    print("Whites turn")
                    print("Wykonaj ruch używając notacji - np. e2 -> enter -> e4")
                    x = input().lower()
                    if x not in short:
                        print("Incorrect input")
                    elif short[x] not in [item[0] for item in self.OB.W_Lmoves] and short[x] not in [item[0] for item in self.enPassantMoves]:
                        print('No legal moves for this position')
                    else:
                        print([long[item[1]] for item in self.OB.W_Lmoves if item[0] == short[x]] + [long[item[1]] for item in self.enPassantMoves if item[0] == short[x]])
                        y = input().lower()
                        if y not in short:
                            print("Incorrect input")
                        elif short[y] not in [item[1] for item in self.OB.W_Lmoves if item[0] == short[x]] and short[y] not in [item[1] for item in self.enPassantMoves if item[0] == short[x]]:
                            print('Illegal move')
                        else:
                            self.makeGameMove(short[x],short[y])
                            game.makeGameMove(short[x],short[y])
                            pyBoard.push(chess.Move.from_uci(x+y))
                            self.OB.Display()

                else:
                    self.enPassantLegalMovesDef()
                    game.enPassantLegalMovesDef()
                    if self.repetitionDraw() == True:
                        break
                    if len(self.getBookMoves(pyBoard)) > 0:
                        x = self.getBookMoves(pyBoard)[0][0]+self.getBookMoves(pyBoard)[0][1]
                        y = self.getBookMoves(pyBoard)[0][2]+self.getBookMoves(pyBoard)[0][3]
                        if (short[x],short[y]) in self.OB.B_Lmoves or (short[x],short[y]) in self.enPassantMoves:
                            pyBoard.push(chess.Move.from_uci(self.getBookMoves(pyBoard)[0]))
                            self.makeGameMove(short[x],short[y])
                            game.makeGameMove(short[x],short[y])
                            self.OB.Display()
                    else:
                        start_time = time.time()
                        move = self.minimaxRoot(self.depth, game, self.ruch)
                        game.makeGameMove(move[0],move[1])
                        self.makeGameMove(move[0],move[1])
                        self.OB.Display()
                        print("--- %s seconds ---" % (time.time() - start_time))
            else:
                if self.ruch == 1:
                    self.enPassantLegalMovesDef()
                    game.enPassantLegalMovesDef()
                    if self.repetitionDraw() == True:
                        break
                    if len(self.getBookMoves(pyBoard)) > 0:
                        x = self.getBookMoves(pyBoard)[0][0] + self.getBookMoves(pyBoard)[0][1]
                        y = self.getBookMoves(pyBoard)[0][2] + self.getBookMoves(pyBoard)[0][3]
                        if (short[x], short[y]) in self.OB.W_Lmoves or (short[x], short[y]) in self.enPassantMoves:
                            pyBoard.push(chess.Move.from_uci(self.getBookMoves(pyBoard)[0]))
                            self.makeGameMove(short[x], short[y])
                            game.makeGameMove(short[x], short[y])
                            self.OB.Display()
                    else:
                        game.enPassantLegalMovesDef()
                        move = self.minimaxRoot(self.depth, game, self.ruch)
                        game.makeGameMove(move[0], move[1])
                        self.makeGameMove(move[0], move[1])
                        self.OB.Display()

                else:
                    self.enPassantLegalMovesDef()
                    if self.repetitionDraw() == True:
                        break
                    print("Blacks turn")
                    print("Wykonaj ruch używając notacji - np. e2 -> enter -> e4")
                    x = input().lower()
                    if x not in short:
                        print("Incorrect input")
                    elif short[x] not in [item[0] for item in self.OB.B_Lmoves] and short[x] not in [item[0] for item in self.enPassantMoves]:
                        print('No legal moves for this position')
                    else:
                        print([long[item[1]] for item in self.OB.B_Lmoves if item[0] == short[x]] + [long[item[1]] for item in self.enPassantMoves if item[0] == short[x]])
                        y = input().lower()
                        if y not in short:
                            print("Incorrect input")
                        elif short[y] not in [item[1] for item in self.OB.B_Lmoves if item[0] == short[x]] and short[y] not in [item[1] for item in self.enPassantMoves if item[0] == short[x]]:
                            print('Illegal move')
                        else:
                            self.makeGameMove(short[x], short[y])
                            game.makeGameMove(short[x], short[y])
                            pyBoard.push(chess.Move.from_uci(x + y))
                            self.OB.Display()

        if self.OB.matedWhite == True:
            print('BLACK WINS')
        elif self.OB.matedBlack == True:
            print("WHITE WINS")
        elif self.OB.draw == True:
            print('DRAW')


    def makeGameMove(self,x,y):
        if (x, y) in self.enPassantMoves:
            self.OB.enPassantMove(x, y)
        elif x == 25 and y == 27:
            self.OB.castleBSC()
        elif x == 25 and y == 23:
            self.OB.castleBLC()
        elif x == 95 and y == 97:
            self.OB.castleWSC()
        elif x == 95 and y == 93:
            self.OB.castleWLC()
        else:
            self.OB.moveMaker(x, y)
        self.kingsRooksMovedCheck(x)
        self.OB.updateMaps()
        self.OB.blackPromotion(self.playerStarts)
        self.OB.whitePromotion(self.playerStarts)
        self.OB.updateMaps()
        self.OB.Lmoves_whiteDef()
        self.OB.Lmoves_blackDef()
        self.OB.mateDrawCheck()
        self.moveHist.append((x, y))
        if self.ruch == 1:
            self.ruch = 0
        else:
            self.ruch = 1

    def getBookMoves(self,pyboard):
        book_moves = []
        with chess.polyglot.open_reader("book.bin") as reader:
            for entry in reader.find_all(pyboard):
                book_moves.append(str(entry.move))
                if len(book_moves) == 3:
                    break
        return book_moves

    def enPassantLegalMovesDef(self):
        self.enPassantMoves = []
        start_state = self.OB.board
        board120WP = array64_to_array120(self.OB.WP)
        board120BP = array64_to_array120(self.OB.BP)
        moves = []
        if self.ruch == 1:
            if len(self.moveHist) > 0:
                if self.moveHist[-1][0] in RANK_7 and (self.moveHist[-1][1] - self.moveHist[-1][0] == 20) and \
                        board120BP[self.moveHist[-1][1]] == 1:
                    if board120WP[self.moveHist[-1][1] + 1] == 1:
                        moves.append((self.moveHist[-1][1] + 1, self.moveHist[-1][1] - 10))
                    if board120WP[self.moveHist[-1][1] - 1] == 1:
                        moves.append((self.moveHist[-1][1] - 1, self.moveHist[-1][1] - 10))
            if len(moves)>0:
                for move in moves:
                    self.OB.enPassantMove(move[0],move[1])
                    self.OB.updateMaps()
                    if self.OB.WK_checked == False:
                        self.enPassantMoves.append(move)
                    self.OB.board = start_state
                    self.OB.updateMaps()

        if self.ruch == 0:
            if len(self.moveHist) > 0:
                if self.moveHist[-1][0] in RANK_2 and (self.moveHist[-1][1] - self.moveHist[-1][0] == -20) and \
                        board120WP[self.moveHist[-1][1]] == 1:
                    if board120BP[self.moveHist[-1][1] + 1] == 1:
                        moves.append((self.moveHist[-1][1] + 1, self.moveHist[-1][1] + 10))
                    if board120BP[self.moveHist[-1][1] - 1] == 1:
                        moves.append((self.moveHist[-1][1] - 1, self.moveHist[-1][1] + 10))
            if len(moves)>0:
                for move in moves:
                    self.OB.enPassantMove(move[0], move[1])
                    self.OB.updateMaps()
                    if self.OB.BK_checked == False:
                        self.enPassantMoves.append(move)
                    self.OB.board = start_state
                    self.OB.updateMaps()

    def repetitionDraw(self):
        self.boardStateList.append(
            [list(self.OB.board), self.OB.W_Lmoves, self.OB.B_Lmoves, self.enPassantMoves, self.OB.castleWSC,
             self.OB.castleWLC, self.OB.castleBSC, self.OB.castleBLC])
        if self.boardStateList.count(
                [list(self.OB.board), self.OB.W_Lmoves, self.OB.B_Lmoves, self.enPassantMoves, self.OB.castleWSC,
                 self.OB.castleWLC, self.OB.castleBSC, self.OB.castleBLC]) == 3:
            self.OB.draw = True
            return True

    def kingsRooksMovedCheck(self,a):
        if a == 21:
            self.BSR_moved = True
        elif a == 28:
            self.BLR_moved = True
        elif a == 25:
            self.BK_moved = True
        elif a == 91:
            self.WLR_moved = True
        elif a == 98:
            self.WSR_moved = True
        elif a == 95:
            self.WK_moved = True
    nodes = 0

    def minimaxRoot(self,depth, board, is_max):
        possibleWmoves = board.OB.W_Lmoves
        possibleBmoves = board.OB.B_Lmoves
        bestMoveFinal = None
        if is_max == 1:
            bestMove = -999999
            possibleMoves = possibleWmoves
            for move in possibleMoves:
                board_save = copy.deepcopy(board)
                board_save.makeGameMove(move[0], move[1])
                value = max(bestMove, self.minimax(depth - 1, board_save, -10000000, 10000000, abs(is_max - 1)))
                if value > bestMove:
                    bestMove = value
                    bestMoveFinal = move
            print(nodes)
            return bestMoveFinal
        else:
            bestMove = 999999
            possibleMoves = possibleBmoves
            for move in possibleMoves:
                board_save = copy.deepcopy(board)
                board_save.makeGameMove(move[0], move[1])
                value = min(bestMove, self.minimax(depth - 1, board_save, -10000000, 10000000, abs(is_max - 1)))
                if value < bestMove:
                    bestMove = value
                    bestMoveFinal = move
            print(nodes)
            return bestMoveFinal

    def minimax(self,depth, board, alpha, beta, is_max):
        global nodes
        nodes+=1
        if (depth == 0):
            board.evaluate()
            return board.evaluation
        possibleWmoves = board.OB.W_Lmoves
        possibleBmoves = board.OB.B_Lmoves
        if is_max == 1:
            bestMove = -999999
            for move in possibleWmoves:
                board_save = copy.deepcopy(board)
                board_save.makeGameMove(move[0], move[1])
                bestMove = max(bestMove, self.minimax(depth - 1, board_save, alpha, beta, abs(is_max - 1)))
                del board_save
                alpha = max(alpha, bestMove)
                if beta <= alpha:
                    return bestMove
            return bestMove
        else:
            bestMove = 999999
            for move in possibleBmoves:
                board_save = copy.deepcopy(board)
                board_save.makeGameMove(move[0], move[1])
                bestMove = min(bestMove, self.minimax(depth - 1, board_save, alpha, beta, abs(is_max - 1)))
                del board_save
                beta = min(beta, bestMove)
                if beta <= alpha:
                    return bestMove
            return bestMove



gameAI = Game_vs_AI(Board(),True,1)
gameAI.start_game_vs_AI()




