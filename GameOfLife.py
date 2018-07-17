from tkinter import *
import time
import threading
#import tkinter which is all I use for this

class board():
    #my board class which controls each square and changing the colors
    def color_change(self):
        #changes color of the object passed in based on its background color
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

def surrounding(obj):
    count = 0
    global NextAlive
    global NextDead
    global Birth
    global Checked

    if obj in Checked:
        return
    if WholeBoard[obj.y][obj.x + 1].alive == True:
        count += 1
    elif WholeBoard[obj.y][obj.x+1] not in Birth and obj.alive == True and WholeBoard[obj.y][obj.x+1].alive == False:
        surrounding(WholeBoard[obj.y][obj.x+1])
    if WholeBoard[obj.y][obj.x - 1].alive == True:
        count += 1
    elif WholeBoard[obj.y][obj.x-1] not in Birth and obj.alive == True and WholeBoard[obj.y][obj.x-1].alive == False:
        surrounding(WholeBoard[obj.y][obj.x-1])
    if WholeBoard[obj.y + 1][obj.x].alive == True:
        count += 1
    elif WholeBoard[obj.y+1][obj.x] not in Birth and obj.alive == True and WholeBoard[obj.y+1][obj.x].alive == False:
        surrounding(WholeBoard[obj.y+1][obj.x])
    if WholeBoard[obj.y - 1][obj.x].alive == True:
        count += 1
    elif WholeBoard[obj.y-1][obj.x] not in Birth and obj.alive == True and WholeBoard[obj.y-1][obj.x].alive == False:
        surrounding(WholeBoard[obj.y-1][obj.x])
    if WholeBoard[obj.y + 1][obj.x + 1].alive == True:
        count += 1
    elif WholeBoard[obj.y+1][obj.x+1] not in Birth and obj.alive == True and WholeBoard[obj.y+1][obj.x+1].alive == False:
        surrounding(WholeBoard[obj.y+1][obj.x+1])
    if WholeBoard[obj.y - 1][obj.x + 1].alive == True:
        count += 1
    elif WholeBoard[obj.y-1][obj.x+1] not in Birth and obj.alive == True and WholeBoard[obj.y-1][obj.x+1].alive == False:
        surrounding(WholeBoard[obj.y-1][obj.x+1])
    if WholeBoard[obj.y - 1][obj.x - 1].alive == True:
        count += 1
    elif WholeBoard[obj.y-1][obj.x-1] not in Birth and obj.alive == True and WholeBoard[obj.y-1][obj.x-1].alive == False:
        surrounding(WholeBoard[obj.y-1][obj.x-1])
    if WholeBoard[obj.y + 1][obj.x - 1].alive == True:
        count += 1
    elif WholeBoard[obj.y+1][obj.x-1] not in Birth and obj.alive == True and WholeBoard[obj.y+1][obj.x-1].alive == False:
        surrounding(WholeBoard[obj.y+1][obj.x-1])
    if obj.alive == False and count == 3:
        Birth.append(obj)
    elif obj.alive == True and count == 2 or count == 3:
        NextAlive.append(obj)
    elif obj.alive == True:
        NextDead.append(obj)
    Checked.append(obj)

def begin():
    global AliveList
    global NextAlive
    global NextDead
    global Birth
    global Checked


    for obj in AliveList:
        surrounding(obj)
    for obj in NextDead:

        obj.color_change()
    AliveList = NextAlive + Birth
    for obj in Birth:
        obj.color_change()

    NextAlive = []
    NextDead = []
    Birth = []
    Checked = []

def auto():
    begin()
    root.after(800,auto)






Checked = []
Birth = []
NextAlive = []
NextDead = []
AliveList = []
length = 30
WholeBoard = [[] for _ in range(length)]
root = Tk()
labels = [[] for _ in range(length)]
step = Button(root, text = "Step", background = 'blue', command=begin)
step.grid(row = length+1, column=length+1)
start = Button(root, text= "Start", background = 'red', command=auto)
start.grid(row = length, column = length+1)
for r in range(length):
    for c in range(length):
        labels[r].append(' ')

for r in range(length):
    for c in range(length):
        bood = board()
        WholeBoard[r].append(bood)


root.mainloop()


