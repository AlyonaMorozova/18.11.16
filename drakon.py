__author__ = 'student'
import turtle as tu
tu.penup()
tu.goto(-200,150)
tu.pendown()
tu.width(2)
tu.color('brown')
tu.speed(6000)
def x(l,n):
    if n==0:
        return
    x(l,n-1)
    tu.right(90)
    y(l,n-1)
    tu.forward(l)
    tu.right(90)

def y (l,n):
    if n==0:
        return
    tu.left(90)
    tu.forward(l)
    x(l,n-1)
    tu.left(90)
    y(l,n-1)

tu.forward(20)
x(10,15)

tu.mainloop()