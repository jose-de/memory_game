from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&") * 2
state = {'mark': None}
hide = [True] * 64

taps = 0
tap_writer = Turtle(visible = False)

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global taps
    taps += 1
    tap_writer.undo()
    tap_writer.write(f'Taps: {taps}', font=('Arial', 14, 'normal'))
 
    spot = index(x, y)
    mark = state['mark']
 
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    if not any(hide):
        draw_win()

def draw_win():
    "Display a win message when all tiles are uncovered."
    onscreenclick(None)  
    win_writer = Turtle(visible=False)
    win_writer.goto(0, 0)
    win_writer.color('green')
    win_writer.write(
        f'You won in {taps} taps!',
        align='center',
        font=('Arial', 24, 'bold'),
    )
    update()

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25,y + 8)
        color('black')
        write(tiles[mark],align = "center", font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
tap_writer.goto(140, 185)
tap_writer.color('black')
tap_writer.write('Taps: 0', font=('Arial', 14, 'normal'))
onscreenclick(tap)
draw()
done()
