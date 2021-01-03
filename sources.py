import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("A MAZE GAME")
wn.setup(1000,700)
wn.tracer(0)


#register shape
turtle.register_shape("IMG/motorbike.gif")
turtle.register_shape("IMG/gas1.gif")
turtle.register_shape("IMG/thewall.gif")
turtle.register_shape("IMG/flag1.gif")

images = ["IMG/motorbike.gif","IMG/gas1.gif","IMG/thewall.gif","IMG/flag1.gif"]
#or
# for image in images:
#     turtle.register_shape(image)

#create pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("IMG/thewall.gif")
        self.color("black")
        self.penup()
        self.speed(0)

#class wall in game
# class Wall(turtle.Turtle):
#     def __init__(self):
#         turtle.Turtle.__init__(self)
#         #self.shape("IMG/thewall.gif")
#         self.shape("IMG/thewall.gif")
#         self.color("brown")
#         self.penup()
#         self.speed(0)

#class Gas
class Gas(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("IMG/gas1.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)
        self.count = 5
    
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
        
#class player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("IMG/motorbike.gif")
        #self.shape("MOTO.gif")
        self.color("blue")
        self.setheading(270)
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        move_to_x = Player.xcor()
        move_to_y = Player.ycor() + 24
        
        
        #check wall
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_down(self):
        move_to_x = Player.xcor()
        move_to_y = Player.ycor() - 24

        #check wall
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_left(self):
        move_to_x = Player.xcor() - 24
        move_to_y = Player.ycor()

        #check wall
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_right(self):
        move_to_x = Player.xcor() + 24
        move_to_y = Player.ycor() 
        #check wall

        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
    
    def is_collision(self,other):
        a = self.xcor() -other.xcor()
        b = self.ycor() -other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

class treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("IMG/flag1.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)
    
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

#create level list
levels = [""]

with open("map.txt") as file:
    level1 = []
    m = 0
    for line in file:
        if m == 0:
            m = int(line)
        else:
            level1.append(line)

#read file map 


#add treasure list
treasures = []
Gass = []
#add maze to mazes function
levels.append(level1)
def setup_maze(level,m):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #get th character
            character = level[y][x]
            #calculate the screen x,y coordinates
            screen_x = -(288) + (x * m)
            screen_y = (288) - (y * m)
            #check if it is an X(WALL)
            if character == "X":
                Pen.goto(screen_x,screen_y)
                Pen.stamp()
                #append wall is check
                walls.append((screen_x,screen_y))
                
            # #check if it is an O(WALL)
            # if character == "O":
            #     Wall.goto(screen_x,screen_y)
            #     Wall.stamp()
            #     #append wall is check
            #     walls.append((screen_x,screen_y))
                
            #check if it is an P(WALL)
            if character == "P":
                Player.goto(screen_x,screen_y)

            #check if it is an T
            if character == "T":
                treasures.append(treasure(screen_x,screen_y))

            #check if it is an G
            if character == "G":
                Gass.append(Gas(screen_x,screen_y))

#create Walls list
walls = []
 
#create class instances

Pen = Pen()
Player = Player()
# Wall = Wall()
#setup the level
setup_maze(levels[1],m)

#keyboard binding
turtle.listen()
turtle.onkey(Player.go_left,"Left")
turtle.onkey(Player.go_right,"Right")
turtle.onkey(Player.go_up,"Up")
turtle.onkey(Player.go_down,"Down")

#turn off screen updates
# wn.tracer(0)
#main game loop
while True:

    for treasure in treasures:
        if Player.is_collision(treasure):

            Player.gold +=treasure.gold
            treasure.destroy()
            treasures.remove(treasure)
    #screen update
    wn.update()
