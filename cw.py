import pgzrun
from random import randint

WIDTH= 400
HEIGHT= 400



def draw():
    r= 255
    g=randint(120,255)
    b=0
    

    width= WIDTH
    height= HEIGHT - 200

    for i in range (20):
        rect= Rect((0,0),(width,height))
        rect.center= 150,150
        screen.draw.rect(rect, (r, g, b ) )


        r -= 10
        g += 10

        width -= 10
        height +=10

pgzrun.go()