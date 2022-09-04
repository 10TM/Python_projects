from turtle import *


def fleur():
    for i in range(300):
        circle(190-i,90,color('red'))
        left(90)
        circle(190-i,90,color('green'))
        left(18)


fleur()
mainloop()