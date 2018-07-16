from tkinter import Tk, Label, RAISED, Button


class board():
    def color_change(self):
        if self.button.cget('bg') == 'black':
            self.button.configure(bg='white')
        else:
            self.button.configure(bg='black')
    def __init__(self):
        self.button = Button(root, padx=10, command=self.color_change, text=labels[r][c], background='black')
        self.button.grid(row=r, column=c)

root = Tk()
length = 15
labels = [[] for _ in range(length)]
for r in range(length):
    for c in range(length):
        labels[r].append(' ')

for r in range(length):
    for c in range(length):
        bood = board()

root.mainloop()
