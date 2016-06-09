import os, random, turtle
stage=[0]

def get_random_word(file_name):
    total_bytes = os.stat(file_name).st_size 
    random_point = random.randint(0, total_bytes)
    file = open(file_name)
    file.seek(random_point)
    file.readline() 
    return file.readline()

#line= get_random_word(r"C:\hangman-python\wordlist.txt")
#print(line)
def pt(word, char, i):
    go_to(-5-(len(word)//2*20) - (len(word)//2*10), -150, 0)
    turtle.penup()
    for j in range(i):
        turtle.forward(20)
        turtle.forward(10)
    turtle.forward(10)
    turtle.pendown()
    turtle.write(char, align='center', font=("Arial", 24, "normal"))
    
def go_to(x, y, p):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(p)
    turtle.pendown()

def hang():
    turtle.speed(2)
    if stage[0]==0:
        go_to(-300,0,0)
        turtle.forward(600)
        go_to(-100,0, 90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(25)
    elif stage[0]==1:
        go_to(0, 150, 0)
        turtle.circle(12.5)
    elif stage[0]==2:
        go_to(0,150, -90)
        turtle.forward(50)
    elif stage[0]==3:
        go_to(0,140, -45)
        turtle.forward(25)
        go_to(0,140, -135)
        turtle.forward(25)
    elif stage[0]==4:
        go_to(0,100, -45)
        turtle.forward(25)
        go_to(0,100, -135)
        turtle.forward(25)
    stage[0]+=1
    return 0

def spaces(word):
    l=len(word)
    if l %2 !=0:
        go_to(-5-(l//2*20) - (l//2*10), -150, 0)
        for i in range(l):
            turtle.forward(20)
            turtle.penup()
            turtle.forward(10)
            turtle.pendown()
    else:
        go_to(-(l//2*20) - (l//2*10), -150, 0)
        for i in range(l):
            turtle.forward(20)
            turtle.penup()
            turtle.forward(10)
            turtle.pendown()

def mistake(word, char):
    go_to(-5-(len(word)//2*20) - (len(word)//2*10), -200, 0)
    turtle.penup()
    for j in range(stage[0]):
        turtle.forward(20)
    turtle.pendown()
    turtle.write(char, align='center', font=("Arial", 8, "normal"))
    hang()

def play(word, out):
    ch=raw_input('Choose letter to type ')
    key=''
    if ch in word:
        for i in range(len(word)):
            if ch==word[i]:
                key+=ch
                pt(word, ch, i)
            else:
                key+=out[i]
        return key
    else:
        mistake(word, ch)
        return out

def main():
    word=get_random_word(r"C:\hangman-python\wordlist.txt").strip('\n').lower()
    print(word)
    #print(len(word))
    print("We have a chosen a "+str(len(word))+" lettered word")
    spaces(word)
    out=' '
    for i in range(len(word)):
        out+='_'
    while out != word and stage[0] <=4:
        print(out)
        out=play(word, out)
    if stage[0] > 4:
        print('Oops. You died')
        turtle.bgcolor('red')
        turtle.exitonclick()
    else:
        print('Congratulations. You guessed correctly ' + word + '!')
        turtle.exitonclick()
if __name__ == '__main__':
    main()

