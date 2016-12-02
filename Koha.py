__author__ = 'student'
import turtle as tu
tu.penup()
tu.goto(-400,0)
tu.pendown()
tu.width(5)
tu.color('red')
def draw_Koh(l, n):
    if n == 1:
        tu.forward(l)
        tu.left(60)
        tu.forward(l)
        tu.right(120)
        tu.forward(l)
        tu.left(60)
        tu.forward(l)
        return
    draw_Koh(l/3,n-1)
    tu.left(60)
    draw_Koh(l/3,n-1)
    tu.right(120)
    draw_Koh(l/3,n-1)
    tu.left(60)
    draw_Koh(l/3,n-1)

draw_Koh(300,4)
