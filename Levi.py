__author__ = 'student'
import turtle as tu
tu.penup()

tu.pendown()
tu.width(2)
tu.color('red')
tu.speed(6000)
def draw_min(l,n):
    if n==1:
        tu.left(45)
        tu.forward(l)
        tu.right(90)
        tu.forward(l)
        tu.left(45)
        return
    tu.left(45)
    draw_min(l,n-1)
    tu.right(90)
    draw_min(l,n-1)
    tu.left(45)
draw_min(5,20)
tu.mainloop()