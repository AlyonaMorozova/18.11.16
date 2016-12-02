__author__ = 'student'
import turtle as tu
tu.penup()
tu.goto(-400,150)
tu.pendown()
tu.width(3)
tu.color('red')
def draw_Koh(l=729, n=1):
    if n == 1:
        tu.forward(l/3)
        tu.left(60)
        tu.forward(l/3)
        tu.right(120)
        tu.forward(l/3)
        tu.left(60)
        tu.forward(l/3)
    else:
        draw_Koh(l/3,n-1)
        tu.left(60)
        draw_Koh(l/3,n-1)
        tu.right(120)
        draw_Koh(l/3,n-1)
        tu.left(60)
        draw_Koh(l/3,n-1)
def snowflake (l=529,n=2):
    for i in range(3):
        draw_Koh(l,n)
        tu.right(120)


snowflake(n=2)
tu.mainloop()



