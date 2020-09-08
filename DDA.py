from tkinter import *
window = Tk()

window.geometry('600x600')
canvas = Canvas(window,height=550,width=550,bg="#ffffff")
canvas.pack()

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = x2 - x1
dy = y2 - y1

steps, x, y = 0, x1, y1

if abs(dx) > abs(dy):
    steps = abs(dx)
else:
    steps = abs(dy)

x_increment = dx/steps
y_increment = dy/steps

for i in range(steps):
    x = x + x_increment
    y = y + y_increment
    print(x,y)
    canvas.create_line(round(x), round(y), round(x)+1, round(y)+1)


window.mainloop()