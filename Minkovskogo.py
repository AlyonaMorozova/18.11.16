__author__ = 'student'
import turtle as tu
tu.penup()
tu.goto(-400,0)
tu.pendown()
tu.width(2)
tu.color('red')
def draw_min(l,n):
    if n==1:
        tu.forward(l)
        return
    draw_min(l/4,n-1)
    tu.left(90)
    draw_min(l/4,n-1)
    tu.right(90)
    draw_min(l/4,n-1)
    tu.right(90)
    draw_min(l/4,n-1)
    draw_min(l/4,n-1)
    tu.left(90)
    draw_min(l/4,n-1)
    tu.left(90)
    draw_min(l/4,n-1)
    tu.right(90)
    draw_min(l/4,n-1)
draw_min(1000,4)
tu.mainloop()

