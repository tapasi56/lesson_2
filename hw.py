import pgzrun
from random import randint

width = 150
height= 400



def draw():
    r = 200
    g = 0
    b = randint(100,250)  


    WIDTH = width + 200
    HEIGHT = height - 100


    for i in range (20):
            rect= Rect((0,0),(width,height))
            rect.center= 120,150
            screen.draw.rect(rect, (r, g, b ) )
            

    r -= 100
    b += 50

    width -= 20
    height += 50


def draw_2():
    r = 100
    g = randint(10,200)
    b = 0

for i in range (20):
            circle= circle()
            circle.center= 120,150
            screen.draw.circle(circle, (r, g, b ) )
            
    

