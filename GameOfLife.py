from tkinter import *


class Board():
    def __init__(self, length):
        self.length = length
        self.wholeBoard = [[] for _ in range(length)]

    def setup(self, root, game, board):
        self.step = Button(root, text="Step", background='blue', command=lambda: game.begin(self.wholeBoard, game))
        self.step.grid(row=2, column=self.length + 1)
        self.start = Button(root, text="Start", background='red',
                            command=lambda: [game.pause(0), game.auto(root, self.wholeBoard, game)])
        self.start.grid(row=0, column=self.length + 1)
        self.stop = Button(root, text="Stop", background='green', command=lambda: game.pause(1))
        self.stop.grid(row=1, column=self.length + 1)
        self.clear = Button(root, text="Clear", background = 'yellow', command=lambda: game.clear(game))
        self.clear.grid(row=3, column=self.length+1)
        for r in range(self.length):
            for c in range(self.length):
                self.button = Piece(root, r, c, game)
                self.wholeBoard[r].append(self.button)


class Piece():
    def __init__(self, root, r, c, game):
        self.button = Button(root, padx=10, command=lambda: self.color_change(game), text=' ', background='black')
        self.button.grid(row=r, column=c)
        self.y = r
        self.x = c
        self.alive = False

    def color_change(self, game):
        if self.button.cget('bg') == 'black':
            self.button.configure(bg='white')
            game.aliveList.append(self)
            self.alive = True
        else:
            self.button.configure(bg='black')
            game.aliveList.remove(self)
            self.alive = False


class Game():
    def __init__(self):
        self.checkedSquares = []
        self.nextAlive = []
        self.nextDead = []
        self.aliveList = []
        self.stopped = True

    def clear(self, game):
        for obj in self.aliveList:
            obj.color_change(game)

    def pause(self, num):
        if num == 0:
            self.stopped = False
        else:
            self.stopped = True

    def auto(self, root, board, game):
        if self.stopped == False:
            self.begin(board, game)
            root.after(800, self.auto, root, board, game)

    def begin(self, board, game):
        for obj in self.aliveList:
            self.surrounding(obj, board)
        for obj in self.nextDead:
            obj.color_change(game)
        for obj in self.nextAlive:
            obj.color_change(game)
        self.nextDead, self.nextAlive, self.checkedSquares = [], [], []

    def surrounding(self, obj, board):
        count = 0
        boardR = board[obj.y][obj.x + 1]
        boardL = board[obj.y][obj.x - 1]
        boardU = board[obj.y + 1][obj.x]
        boardD = board[obj.y - 1][obj.x]
        boardRU = board[obj.y + 1][obj.x + 1]
        boardRD = board[obj.y - 1][obj.x + 1]
        boardLU = board[obj.y + 1][obj.x - 1]
        boardLD = board[obj.y - 1][obj.x - 1]

        if obj in self.checkedSquares:
            return
        if boardR.alive == True:
            count += 1
        elif boardR not in self.checkedSquares and boardR.alive == False and obj.alive == True:
            self.surrounding(boardR, board)
        if boardL.alive == True:
            count += 1
        elif boardL not in self.checkedSquares and boardL.alive == False and obj.alive == True:
            self.surrounding(boardL, board)
        if boardU.alive == True:
            count += 1
        elif boardU not in self.checkedSquares and boardU.alive == False and obj.alive == True:
            self.surrounding(boardU, board)
        if boardD.alive == True:
            count += 1
        elif boardD not in self.checkedSquares and boardD.alive == False and obj.alive == True:
            self.surrounding(boardD, board)
        if boardRU.alive == True:
            count += 1
        elif boardRU not in self.checkedSquares and boardRU.alive == False and obj.alive == True:
            self.surrounding(boardRU, board)
        if boardRD.alive == True:
            count += 1
        elif boardRD not in self.checkedSquares and boardRD.alive == False and obj.alive == True:
            self.surrounding(boardRD, board)
        if boardLU.alive == True:
            count += 1
        elif boardLU not in self.checkedSquares and boardLU.alive == False and obj.alive == True:
            self.surrounding(boardLU, board)
        if boardLD.alive == True:
            count += 1
        elif boardLD not in self.checkedSquares and boardLD.alive == False and obj.alive == True:
            self.surrounding(boardLD, board)
        if obj.alive is True and (count < 2 or count > 3):
            self.nextDead.append(obj)
        elif obj.alive == False and count == 3:
            self.nextAlive.append(obj)
        self.checkedSquares.append(obj)


if __name__ == "__main__":
    root = Tk()
    game = Game()
    board = Board(30)
    board.setup(root, game, board)
    root.mainloop()
