# GameOfLife
John Conway's Game of Life made in Python with Tkinter.
My First Python Project made with Tkinter.
White Blocks are alive and black blocks are dead. Blocks can be turned alive/dead at anytime by clicking on them. 
Start Button auto runs the game.
Stop Button pauses the auto run and can be continuted again by pressing the start button. 
Step Button makes one move at a time. 
Problems I ran into included:
1. Needing to run multiple functions with one button: Fixed by using lambda
2. Having a true loop while running Tkinter: Fixed by using the Tkinter after function recursively(Couldn't use threading because
I call Tkinter methods within my while True loop which can cause crashes and unexpected behavior).
3. Learning Tkinter methods such as cget to find the background color of buttons.
