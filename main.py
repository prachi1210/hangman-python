import os, random,turtle

stage=0  
def get_random_line(file_name):
    total_bytes = os.stat(file_name).st_size 
    random_point = random.randint(0, total_bytes)
    file = open(file_name)
    file.seek(random_point)
    file.readline() # skip this line to clear the partial line
    return file.readline()

#line= get_random_line(r"C:\Udacity\hangman-python\wordlist.txt")
#print(line)

def go_to(x, y, p):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(p)
    turtle.pendown()

def hang(stage):
    turtle.speed(2)
    if stage==0:
        go_to(-300,0,0)
        turtle.forward(600)
        go_to(-100,0, 90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(25)
    elif stage==1:
        go_to(0, 150, 0)
        turtle.circle(12.5)
    elif stage==2:
        go_to(0,150, -90)
        turtle.forward(50)
    elif stage==3:
        go_to(0,140, -45)
        turtle.forward(25)
        go_to(0,140, -135)
        turtle.forward(25)
    elif stage==4:
        go_to(0,100, -45)
        turtle.forward(25)
        go_to(0,100, -135)
        turtle.forward(25)
    return 0
stage = 0
while(stage<5):
    hang(stage)
    stage+=1
    
