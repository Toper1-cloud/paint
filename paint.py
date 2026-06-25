from turtle import *
t = Turtle()


print('Выберите форму фигурки:\n')
print('1 - arrow (стрелка)')
print('2 - turtle (черепашка)')
print('3 - circle (круг)')
print('4 - square (квадрат)')
print('5 - triangle (треугольник)\n')

print('Ваш выбор (введите цифру):')
print('Your choice (enter a number):')

choice = input('')

if choice == '1':
    t.shape("arrow")
elif choice == '2':
    t.shape("turtle")
elif choice == '3':
    t.shape("circle")
elif choice == '4':
    t.shape("square")
elif choice == '5':
    t.shape("triangle")
else:
    print('Неверный выбор, форма не изменена.\n')

t.color('black')
print('Чем ниже скорость, тем быстрее фигурка… и больше багов!')
print('Lower speed means a faster figure… and more bugs!')
print('Введите скорость (0-10):')
print('Enter the speed (0-10):')
t.speed(int(input('')))


def draw(x, y):
    t.goto(x, y)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


t.ondrag(draw)

window = t.getscreen()
window.onscreenclick(move)

step = 10

def make_move_right():
    x = t.xcor()
    y = t.ycor()
    t.goto(x + step, y)
def make_move_left():
    x = t.xcor()
    y = t.ycor()
    t.goto(x - step, y)
def make_move_down():
    x = t.xcor()
    y = t.ycor()
    t.goto(x, y - step)
def make_move_up():
    x = t.xcor()
    y = t.ycor()
    t.goto(x, y + step)

def pen_begin_fill():
    t.begin_fill()
def pen_end_fill():
    t.end_fill()



def make_red():
    t.color('red')
def make_orange():
    t.color('orange')
def make_gold():
    t.color('gold')
def make_yellow():
    t.color('yellow')
def make_green():
    t.color('green')
def make_lime():
    t.color('lime')
def make_cyan():
    t.color('cyan')
def make_dodgerblue():
    t.color('dodgerblue')
def make_blue():
    t.color('blue')
def make_mediumpurple():
    t.color('mediumpurple')
def make_black():
    t.color('black')
def make_white():
    t.color('white')






window.listen()


window.onkey(make_move_right, 'd')
window.onkey(make_move_left, 'a')
window.onkey(make_move_down, 's')
window.onkey(make_move_up, 'w')

window.onkey(make_move_right, 'Right')
window.onkey(make_move_left, 'Left')
window.onkey(make_move_down, 'Down')
window.onkey(make_move_up, 'Up')

window.onkey(make_red, '1')
window.onkey(make_orange, '2')
window.onkey(make_gold, '3')
window.onkey(make_yellow, '4')
window.onkey(make_green, '5')
window.onkey(make_lime, '6')
window.onkey(make_cyan, '7')
window.onkey(make_dodgerblue, '8')
window.onkey(make_blue, '9')
window.onkey(make_mediumpurple, '0')
window.onkey(make_black, 'r')
window.onkey(make_white, 'f')

window.onkey(pen_begin_fill, 'q')
window.onkey(pen_end_fill, 'e')
print('Русский:')
print('1 - выбрать красный цвет')
print('2 - выбрать оранжевый цвет')
print('3 - выбрать золотой цвет')
print('4 - выбрать жёлтый цвет')
print('5 - выбрать зелёный цвет')
print('6 - выбрать лаймовый цвет')
print('7 - выбрать голубой цвет')
print('8 - выбрать светло синий цвет')
print('9 - выбрать синий цвет')
print('0 - выбрать фиолетовый цвет')
print('й - начать заливку')
print('у - закончить заливку')
print('ц - вверх')
print('ф - влево')
print('ы - вниз')
print('в - вправо')
print('нажать в любое место ЛКМ - перенос мышки в ту точку')
print('стрелка вверх - вверх')
print('стрелка влево - влево')
print('стрелка вниз - вниз')
print('стрелка вправо - вправо')

print('English:')
print('1 - choose red color')
print('2 - choose orange color')
print('3 - choose gold color')
print('4 - choose yellow color')
print('5 - choose green color')
print('6 - choose lime color')
print('7 - choose cyan color')
print('8 - choose light blue color')
print('9 - choose blue color')
print('0 - choose purple color')
print('q - start filling')
print('e - stop filling')
print('w - move up')
print('a - move left')
print('s - move down')
print('d - move right')
print('click anywhere with LMB - move the mouse to that point')
print('Up arrow - move up')
print('Left arrow - move left')
print('Down arrow - move down')
print('Right arrow - move right')
