import numpy as np
from BoardClass import Board
short = {'a8':21,'b8':22,'c8':23,'d8':24,'e8':25,'f8':26,'g8':27,'h8':28,
         'a7':31,'b7':32,'c7':33,'d7':34,'e7':35,'f7':36,'g7':37,'h7':38,
         'a6':41,'b6':42,'c6':43,'d6':44,'e6':45,'f6':46,'g6':47,'h6':48,
         'a5':51,'b5':52,'c5':53,'d5':54,'e5':55,'f5':56,'g5':57,'h5':58,
         'a4':61,'b4':62,'c4':63,'d4':64,'e4':65,'f4':66,'g4':67,'h4':68,
         'a3':71,'b3':72,'c3':73,'d3':74,'e3':75,'f3':76,'g3':77,'h3':78,
         'a2':81,'b2':82,'c2':83,'d2':84,'e2':85,'f2':86,'g2':87,'h2':88,
         'a1':91,'b1':92,'c1':93,'d1':94,'e1':95,'f1':96,'g1':97,'h1':98}
class Game:

    def __init__(self,OB,ruch=1,moveHist = [],draw = False):
        self.OB = OB
        self.ruch = ruch
        self.moveHist = moveHist
        self.draw = draw

    def start_game(self):
        self.OB.updateMaps()
        self.OB.Display()
        while True:
            if self.OB.matedWhite == False and self.OB.matedBlack == False and self.OB.staleWhite == False and self.OB.staleBlack == False:
                if self.ruch == 1:
                    print("Whites turn")
                    print("Wykonaj ruch używając notacji - np. e2 -> enter -> e4")
                    x = input().lower()
                    if x not in short:
                        print("Incorrect input")
                    elif short[x] not in [item[0] for item in self.OB.W_Lmoves]:
                        print('No legal moves for this position')
                    else:
                        y = input().lower()
                        if y not in short:
                            print("Incorrect input")
                        elif short[y] not in [item[1] for item in self.OB.W_Lmoves]:
                            print('Illegal move')
                        else:
                            self.OB.moveMaker(short[x],short[y])
                            self.OB.updateMaps
                            self.OB.Lmoves_whiteDef()
                            self.OB.Lmoves_blackDef()
                            self.OB.matePatCheck()
                            if self.ruch == 1:
                                self.ruch = 0
                            else:
                                self.ruch = 1
                            self.OB.Display()
                else:
                    print("Blacks turn")
                    print("Wykonaj ruch używając notacji - np. e2 -> enter -> e4")
                    x = input().lower()
                    if x not in short:
                        print("Incorrect input")
                    elif short[x] not in [item[0] for item in self.OB.B_Lmoves]:
                        print('No legal moves for this position')
                    else:
                        y = input().lower()
                        if y not in short:
                            print("Incorrect input")
                        elif short[y] not in [item[1] for item in self.OB.B_Lmoves]:
                            print('Illegal move')
                        else:
                            self.OB.moveMaker(short[x], short[y])
                            self.OB.updateMaps
                            self.OB.Lmoves_whiteDef()
                            self.OB.Lmoves_blackDef()
                            self.OB.matePatCheck()

                            if self.ruch == 1:
                                self.ruch = 0
                            else:
                                self.ruch = 1
                            self.OB.Display()





board = Board()
game1 = Game(board)
game1.start_game()
