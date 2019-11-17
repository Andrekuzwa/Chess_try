from sys import maxsize  # infinity (a really big number)


class Node(object):
    def __init__(self, i_depth, i_playerNum, i_sticksRemaining, i_value=0):
        self.i_depth = i_depth  # how deep are we in the tree (decreases every iteration
        self.i_playerNum = i_playerNum  # (either +1 or -1)
        self.i_sticksRemaining = i_sticksRemaining  # amount of sticks left
        self.i_value = i_value  # gamestate: -inf, 0 or +inf
        self.children = []
        self.CreateChildren()

    def CreateChildren(self):
        if self.i_depth >= 0:  # have we passed the DEPTH of 0 (stop of recursion)
            for i in range(1, 3):  # (how many stick are we gonna remove)
                v = self.i_sticksRemaining - i
                self.children.append(Node(self.i_depth - 1, -self.i_playerNum, v,
                                          self.RealVal(v)))  # add to childrens list, depth goes down, player switches

    def RealVal(self, value):
        if (value == 0):
            return maxsize * self.i_playerNum  # e.g. bullybot
        elif (value < 0):
            return maxsize * -self.i_playerNum  # this bot
        return 0


def MinMax(node, i_depth, i_playerNum):
    if (i_depth == 0) or (abs(node.i_value) == maxsize):  # have we reached depth 0 or the best node?
        return node.i_value  # passing the best node up to the current node

    i_bestValue = maxsize * -i_playerNum  # possitive p

    for i in range(len(node.children)):
        child = node.children[i]
        i_val = MinMax(child, i_depth - 1, -i_playerNum)
        if (abs(maxsize * i_playerNum - i_val) < abs(maxsize * i_playerNum - i_bestValue)):
            i_bestValue = i_val  # store the found best value in this variable

    # debug
    return i_bestValue


def WinCheck(i_sticks, i_playerNum):
    if i_sticks <= 0:
        print("*" * 30)
        if i_playerNum > 0:
            if i_sticks == 0:
                print("\tHuman won!")
            else:
                print("\tToo many chosen, you lost!")
        else:
            if i_sticks == 0:
                print("\tComputer won!")
            else:
                print("\tComputer done did fucked up..")
        print("*" * 30)
        return 0
    return 1


if __name__ == '__main__':
    i_stickTotal = 11
    i_depth = 4
    i_curPlayer = 1
    print("""Instructions: Be the player to pick up the last stick.
                \t\t\tYou can only pick up one (1) or two (2) at a time.""")

    while (i_stickTotal > 0):
        ## HUMAN TURN
        print("\n%d sticks remain. How many will you pick up?" % i_stickTotal)
        i_choice = input("\n1 or 2:                 ")
        # i_choice = 1 debug
        i_stickTotal -= int(float(i_choice))  # store choice of human
        ## COMPUTER TURN
        if WinCheck(i_stickTotal, i_curPlayer):
            i_curPlayer *= -1
            node = Node(i_depth, i_curPlayer, i_stickTotal)
            bestChoice = -100
            i_bestValue = -i_curPlayer * maxsize
            ## DETERMINE NUMBER OF STICKS TO REMOVE
            for i in range(len(node.children)):
                n_child = node.children[i]
                i_val = MinMax(n_child, i_depth, -i_curPlayer)
                if (abs(i_curPlayer * maxsize - i_val) <=
                        abs(i_curPlayer * maxsize - i_bestValue)):
                    i_bestValue = i_val
                    bestChoice = i
            bestChoice += 1
            print("Comp chooses: " + str(bestChoice) + "\tBased on value: " + str(i_bestValue))
            i_stickTotal -= bestChoice
            WinCheck(i_stickTotal, i_curPlayer)
            i_curPlayer *= -1  # switch players



class Node:
    def __init__(self,depth,gameBoard,value=0):
        self.depth = depth
        self.value = value
        self.gameBoard = gameBoard
        self.children = []
        self.CreateKids()

    def CreateKids(self):
        if self.depth >= 0:
            if self.gameBoard.ruch == 1:
                if len(self.gameBoard.OB.W_Lmoves) > 0:
                    for move in self.gameBoard.OB.W_Lmoves:
                        state = self.gameBoard
                        state.makeGameMove(move[0],move[1])
                        print('WW')
                        self.children.append(Node(self.depth-1,state))
            elif self.gameBoard.ruch == 0:
                if len(self.gameBoard.OB.B_Lmoves) > 0:
                    for move in self.gameBoard.OB.B_Lmoves:
                        state = self.gameBoard
                        state.makeGameMove(move[0], move[1])
                        print('BB')
                        self.children.append(Node(self.depth-1,state))

        else:
            return None

#node = Node(1,Game(Board()))


def minimax(depth,board,alpha,beta,is_max):
    if (depth == 0):
        board.OB.evaluate()
        return board.OB.evaluation
    possibleWmoves = board.OB.W_Lmoves
    possibleBmoves = board.OB.B_Lmoves
    if is_max == 1:
        bestMove = -999999
        for move in possibleWmoves:
            board_save = board
            board_save.makeGameMove(move[0],move[1])
            bestMove = max(bestMove,minimax(depth-1,board_save,alpha,beta,abs(is_max-1)))
            alpha = max(alpha,bestMove)
            if beta <= alpha:
                return bestMove
        return bestMove
    else:
        bestMove = 999999
        for move in possibleBmoves:
            board_save = board
            board_save.makeGameMove(move[0],move[1])
            bestMove = min(bestMove,minimax(depth-1,board_save,alpha,beta,abs(is_max-1)))
            beta = min(beta,bestMove)
            if beta <= alpha:
                return bestMove
        return bestMove


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
        board_save = board
        board_save.makeGameMove(move[0],move[1])
        value = max(bestMove,minimax(depth-1,board_save,-10000000,10000000,abs(is_max-1)))
        if value > bestMove:
            print("Best score",bestMove)
            print("Best move", str(bestMoveFinal))
            bestMove = value
            bestMoveFinal = move
    return bestMoveFinal
