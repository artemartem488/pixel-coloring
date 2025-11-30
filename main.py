import turtle

def move_up():
    pen.setheading(90)
    pen.forward(10)

def move_down():
    pen.setheading(270)
    pen.forward(10)

def move_right():
    pen.setheading(0)
    pen.forward(10)

def move_left():
    pen.setheading(180)
    pen.forward(10)

def enter_chvet():
    input_color = turtle.textinput('Вопрос', 'В какой цвет закрасить?')
    x = (pen.xcor() // 50) * 50
    y = (pen.ycor() // 50) * 50
    draw_sqrt(x, y, input_color)
    screen.listen()
    pen.showturtle()

def draw_sqrt(x, y, color, size=50):
    try:
        pen.color(color)
        pen.up()
        pen.goto(x, y)
        pen.setheading(90)
        pen.fillcolor(color)
        pen.begin_fill()
        for i in range(4):
            pen.forward(size)
            pen.right(90)
        pen.end_fill()
    except:
        print('Ошибка')

def end_run():
    turtle.bye()

screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.title('Пиксельная раскраска')
screen.bgcolor("lightgray")

pen = turtle.Pen()
pen.pensize(2)
pen.pencolor('black')
pen.speed(100)
pen.hideturtle()

for i in range(-250, 250, 50):
    pen.up()
    pen.goto(i, -250)
    pen.down()
    pen.goto(i, 500)

for i in range(-250, 250, 50):
    pen.up()
    pen.goto(-250, i)
    pen.down()
    pen.goto(500, i)

pen.showturtle()
pen.up()
pen.home()


screen.listen()
screen.onkey(move_right, 'Right')
screen.onkey(move_left, 'Left')
screen.onkey(move_up, 'Up')
screen.onkey(move_down, 'Down')
screen.onkey(enter_chvet, 'Return')
screen.onkey(end_run, 'space')      

turtle.done()

