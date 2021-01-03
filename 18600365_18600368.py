#####################################
# Breadth First Search / Flood fill
# Davis MT
# 28.01.2018
#####################################

import turtle
from tkinter import *
import time
import sys
from collections import deque

wn = turtle.Screen()               # define the turtle screen
wn.bgcolor("White")                # set the background colour
wn.title("A BFS Maze Solving Program")
wn.setup(1300,700)                  # setup the dimensions of the working window

turtle.register_shape("IMG/motorbike.gif")
turtle.register_shape("IMG/gas1.gif")
turtle.register_shape("IMG/thewall.gif")
turtle.register_shape("IMG/flag1.gif")

# this is the class for the Maze
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("IMG/thewall.gif")
        self.color("black")
        self.penup()
        self.speed(0)

class Gas(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("IMG/gas1.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.count = 5
    
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
    
        
# this is the class for the finish line - green square in the maze
class draw(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("IMG/flag1.gif")
        self.color("green")
        self.penup()
        self.speed(0)

class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


# this is the class for the yellow or turtle
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("IMG/motorbike.gif")
        #self.shape("IMG/MOTO.gif")
        self.color("blue")
        self.setheading(270)
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)



def setup_maze(grid):                          # define a function called setup_maze
    global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
    for y in range(len(grid)):                 # read in the grid line by line
        for x in range(len(grid[y])):          # read each cell in the line
            character = grid[y][x]             # assign the varaible "character" the the x and y location od the grid
            screen_x = -288 + (x * 24)         # move to the x location on the screen staring at -588
            screen_y = 288 - (y * 24)          # move to the y location of the screen starting at 288

            if character == "+":
                Pen.goto(screen_x, screen_y)         # move pen to the x and y locaion and
                Pen.stamp()                          # stamp a copy of the turtle on the screen
                walls.append((screen_x, screen_y))    # add coordinate to walls list

            if character == " " or character == "e":
                path.append((screen_x, screen_y))     # add " " and e to path list

            if character == "e":
                draw.color("purple")
                draw.goto(screen_x, screen_y)       # send green sprite to screen location
                #end_x, end_y = screen_x,screen_y     # assign end locations variables to end_x and end_y
                draw.stamp()
                draw.color("green")
                
            if character == "g":
                 Gas.goto(screen_x,screen_y)
                 end_x, end_y = screen_x,screen_y
                 Gas.stamp()
                 
                 
            if character == "s":
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                Player.goto(screen_x, screen_y)
                
            if character == "g":
                end_x, end_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                Gass.append(end_x,end_y)


def endProgram():
    wn.exitonclick()
    sys.exit()

def search(x,y,n):
    frontier.append((x, y))
    solution[x,y] = x,y

    while len(frontier) > 0:          # exit while loop when frontier queue equals zero
        #time.sleep(0.2)
        x, y = frontier.popleft()     # pop next entry in the frontier queue an assign to x and y location

        if(x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
            cell = (x - 24, y)
            solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
            frontier.append(cell)   # add cell to frontier list
            visited.add((x-24, y))  # add cell to visited list

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
            cell = (x, y - 24)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y - 24))
            print(solution)

        if(x + 24, y) in path and (x + 24, y) not in visited:   # check the cell on the  right
            cell = (x + 24, y)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x +24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
            cell = (x, y + 24)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y + 24))
        green.goto(x,y)


def backRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):    # stop loop when current cells == start cell
        yellow.goto(solution[x , y])
        # move the yellow sprite to the key value of solution ()
        yellow.stamp()
        x, y = solution[x, y]             # "key value" now becomes the new key
        Player.goto(solution[x, y])
        time.sleep(0.2)

        
# set up classes
Pen = Pen()
Player = Player()
green = Green()
draw = draw()
yellow = Yellow()
Gas = Gas()
# setup lists
walls = []
path = []
visited = set()
frontier = deque()
solution = {}                           # solution dictionary
grid = []
Gass = []
n = 7

# readfile map.txt
with open("map.txt") as file:
    m = 0
    for line in file:
        if m == 0:
            m = int(line)
        else:
            grid.append(line)

def BFS_SEARCH():
    search(start_x,start_y,n)
    backRoute(end_x, end_y)
top = Tk()
B = Button(top,text="BFS",command=BFS_SEARCH)


# main program starts here ####
setup_maze(grid)
B.pack()
top.mainloop()
wn.exitonclick()
