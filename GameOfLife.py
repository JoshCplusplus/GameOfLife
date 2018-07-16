from tkinter import *


class board():
    def color_change(self):
        if self.button.cget('bg') == 'black':
            self.button.configure(bg='white')
            AliveList.append(self)
            self.alive = True
        else:
            self.button.configure(bg='black')
            AliveList.remove(self)
            self.alive = False
    def __init__(self):
        self.button = Button(root, padx=10, command=self.color_change, text=labels[r][c], background='black')
        self.button.grid(row=r, column=c)
        self.x = c
        self.y = r
        self.alive = False

def begin():
    global AliveList
    global NextAlive
    global NextDead

    for obj in AliveList:
        print(obj)
        count = 0
        if WholeBoard[obj.y][obj.x+1].alive == True:
            count += 1
        if WholeBoard[obj.y][obj.x-1].alive == True:
            count += 1
        if WholeBoard[obj.y+1][obj.x].alive == True:
            count += 1
        if WholeBoard[obj.y-1][obj.x].alive == True:
            count += 1
        if WholeBoard[obj.y+1][obj.x+1].alive == True:
            count += 1
        if WholeBoard[obj.y-1][obj.x+1].alive == True:
            count += 1
        if WholeBoard[obj.y-1][obj.x-1].alive == True:
            count += 1
        if WholeBoard[obj.y+1][obj.x-1].alive == True:
            count += 1
        if count == 2 or count == 3:
            NextAlive.append(obj)
        else:
            NextDead.append(obj)
    for obj in NextDead:
        obj.color_change()
    AliveList = NextAlive
    NextAlive = []
    NextDead = []






NextAlive = []
NextDead = []
AliveList = []
length = 15
WholeBoard = [[] for _ in range(length)]
root = Tk()
labels = [[] for _ in range(length)]
start = Button(root, text = "Start", background = 'blue', command=begin)
start.grid(row = length+1, column=length+1)
for r in range(length):
    for c in range(length):
        labels[r].append(' ')

for r in range(length):
    for c in range(length):
        bood = board()
        WholeBoard[r].append(bood)

root.mainloop()


