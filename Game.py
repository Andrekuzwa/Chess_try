import numpy as np
import copy
from BoardClass import Board

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


class Game:

    def __init__(self,OB,ruch=1,moveHist = [],draw = False,enPassantMoves = [],boardStateList=[]):
        self.OB = OB
        self.ruch = ruch
        self.moveHist = moveHist
        self.draw = draw
        self.enPassantMoves = enPassantMoves
        self.boardStateList = boardStateList
        self.OB.updateMaps()

    def start_game(self):
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
        self.OB.blackPromotion()
        self.OB.updateMaps()
        self.OB.Lmoves_whiteDef()
        self.OB.Lmoves_blackDef()
        self.OB.mateDrawCheck()
        self.moveHist.append((x, y))
        if self.ruch == 1:
            self.ruch = 0
        else:
            self.ruch = 1


    # def makeGameMove(self,x,y):
    #     if (short[x], short[y]) in self.enPassantMoves:
    #         self.OB.enPassantMove(short[x], short[y])
    #     elif short[x] == 25 and short[y] == 27:
    #         self.OB.castleBSC()
    #     elif short[x] == 25 and short[y] == 23:
    #         self.OB.castleBLC()
    #     elif short[x] == 95 and short[y] == 97:
    #         self.OB.castleWSC()
    #     elif short[x] == 95 and short[y] == 93:
    #         self.OB.castleWLC()
    #     else:
    #         self.OB.moveMaker(short[x], short[y])
    #     self.kingsRooksMovedCheck(short[x])
    #     self.OB.updateMaps()
    #     self.OB.blackPromotion()
    #     self.OB.updateMaps()
    #     self.OB.Lmoves_whiteDef()
    #     self.OB.Lmoves_blackDef()
    #     self.OB.mateDrawCheck()
    #     self.moveHist.append((short[x], short[y]))
    #     if self.ruch == 1:
    #         self.ruch = 0
    #     else:
    #         self.ruch = 1
    #
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

#
# game1 = Game(Board())
# game1.start_game()




# def minimaxRoot(depth,board,ruch):
#     if ruch == 1:
#         L_moves = board.OB.W_Lmoves
#         bestScore = -999999
#     else:
#         L_moves = board.OB.B_Lmoves
#         bestScore = 999999
#     bestMove = None
#     for move in L_moves:
#         board_save = board
#         board_save.makeGameMove(move[0],move[1])
#         value = max()

def minimaxRoot(depth,board,is_max):
    possibleWmoves = board.OB.W_Lmoves
    possibleBmoves = board.OB.B_Lmoves
    bestMove = -999999
    bestMoveFinal = None
    nodes = 0
    if is_max == 1:
        possibleMoves = possibleWmoves
    else:
        possibleMoves = possibleBmoves
    for move in possibleMoves:
        board_save = copy.deepcopy(board)
        board_save.makeGameMove(move[0],move[1])
        board_save.OB.Display()
        value = max(bestMove,minimax(depth-1,board_save,-10000000,10000000,abs(is_max-1)))
        if value > bestMove:
            print("Best score",bestMove)
            print("Best move", str(bestMoveFinal))
            bestMove = value
            bestMoveFinal = move
    return bestMoveFinal

nodes = 0
def minimax(depth,board,alpha,beta,is_max):
    global nodes
    nodes+=1
    if (depth == 0):
        board.OB.evaluate()
        return board.OB.evaluation
    possibleWmoves = board.OB.W_Lmoves
    possibleBmoves = board.OB.B_Lmoves
    if is_max == 1:
        bestMove = -999999
        for move in possibleWmoves:
            board_save = copy.deepcopy(board)
            board_save.makeGameMove(move[0],move[1])
            board_save.OB.Display
            bestMove = max(bestMove,minimax(depth-1,board_save,alpha,beta,abs(is_max-1)))
            del board_save
            alpha = max(alpha,bestMove)
            if beta <= alpha:
                return bestMove
        return bestMove
    else:
        bestMove = 999999
        for move in possibleBmoves:
            board_save = copy.deepcopy(board)
            board_save.makeGameMove(move[0],move[1])
            board_save.OB.Display
            bestMove = min(bestMove,minimax(depth-1,board_save,alpha,beta,abs(is_max-1)))
            del board_save
            beta = min(beta,bestMove)
            if beta <= alpha:
                return bestMove
        return bestMove

# class Node:
#     def __init__(self,depth,gameBoard,value=0):
#         self.depth = depth
#         self.value = value
#         self.gameBoard = gameBoard
#         self.children = []
#         self.CreateKids()
#
#     def CreateKids(self):
#         if self.depth >= 0:
#             if self.gameBoard.ruch == 1:
#                 if len(self.gameBoard.OB.W_Lmoves) > 0:
#                     for move in self.gameBoard.OB.W_Lmoves:
#                         state = self.gameBoard
#                         state.makeGameMove(move[0],move[1])
#                         print('WW')
#                         self.children.append(Node(self.depth-1,state))
#             elif self.gameBoard.ruch == 0:
#                 if len(self.gameBoard.OB.B_Lmoves) > 0:
#                     for move in self.gameBoard.OB.B_Lmoves:
#                         state = self.gameBoard
#                         state.makeGameMove(move[0], move[1])
#                         print('BB')
#                         self.children.append(Node(self.depth-1,state))
#
#         else:
#             return None
#
# #node = Node(1,Game(Board()))
#



game = Game(Board())
print(minimaxRoot(2,game,game.ruch))
print("Number of nodes:",nodes)
#
# class Minimax:
#     def __init__(self,position,depth,alpha,beta,maxPlayer):
#         self.position = position
#         self.depth = depth
#         self.alpha = alpha
#         self.beta = beta
#         self.maxPlayer = maxPlayer
#         self.children = []
#         self.value = self.CreateChildren()
#         self.bestMove = None
#
#     def CreateChildren(self):
#         if self.depth == 0:
#             self.position.OB.evaluate()
#             return self.position.OB.evaluation
#         if self.maxPlayer == 1:
#             maxEval = -999999
#             for move in self.position.OB.W_Lmoves:
#                 board_save = self.position
#                 board_save.makeGameMove(move[0],move[1])
#                 self.children.append(Minimax(board_save,self.depth-1,self.alpha,self.beta,0))
#                 maxEval = max([i.value for i in self.children])
#                 bestMove = [i.position.moveHist[-1] for i in self.children if i.value == maxEval]
#                 self.alpha = max(self.alpha,maxEval)
#                 if self.beta <= self.alpha:
#                     break
#             return bestMove
#         else:
#             minEval = 999999
#             for move in self.position.OB.W_Lmoves:
#                 board_save = self.position
#                 board_save.makeGameMove(move[0],move[1])
#                 self.children.append(Minimax(board_save,self.depth-1,self.alpha,self.beta,1))
#                 bestMove = [i.position.moveHist[-1] for i in self.children if i.value == minEval]
#                 minEval = min([i.value for i in self.children])
#                 self.beta = min(self.beta,minEval)
#                 if self.beta <= self.alpha:
#                     break
#             return bestMove
#
# game = Game(Board())
# #max = Minimax(game,1,-9999999,9999999,1)
# # print(max.value)
#
# game_list = []
# for i in game.OB.W_Lmoves:
#     game_list.append(game)
#     game_list[-1].makeGameMove(i[0],i[1])
#
# for i in game_list:
#     game_list[-1].OB.Display()
