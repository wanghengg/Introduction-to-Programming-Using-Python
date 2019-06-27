# -*_ coding: utf-8 -*-

import turtle

turtle.setup(1800, 500)
t1 = turtle.Turtle()
t1.pensize(5)

#绘制三角形
t1.penup()
t1.goto(-725, -80)
t1.pendown()
t1.color("red")
t1.fillcolor("red")
t1.begin_fill()
t1.seth(60)
t1.forward(250)
t1.right(120)
t1.forward(250)
t1.right(120)
t1.forward(250)
t1.end_fill()

#绘制正方形
t1.penup()
t1.goto(-425, -80)
t1.pendown()
t1.color("blue")
t1.seth(90)
t1.fillcolor("blue")
t1.begin_fill()
t1.forward(250)
t1.right(90)
t1.forward(250)
t1.right(90)
t1.forward(250)
t1.right(90)
t1.forward(250)
t1.end_fill()

#绘制五边形
t1.penup()
t1.goto(-100, -80)
t1.color("green")
t1.pendown()
t1.seth(108)
t1.fillcolor("green")
t1.begin_fill()
t1.forward(200)
t1.right(72)
t1.forward(200)
t1.right(72)
t1.forward(200)
t1.right(72)
t1.forward(200)
t1.right(72)
t1.forward(200)
t1.end_fill()

#绘制六边形
t1.penup()
t1.goto(225, -80)
t1.color("yellow")
t1.pendown()
t1.seth(120)
t1.fillcolor("yellow")
t1.begin_fill()
t1.forward(150)
t1.right(60)
t1.forward(150)
t1.right(60)
t1.forward(150)
t1.right(60)
t1.forward(150)
t1.right(60)
t1.forward(150)
t1.right(60)
t1.forward(150)
t1.end_fill()

#绘制八边形
t1.penup()
t1.goto(550, -80)
t1.pendown()
t1.color("purple")
t1.fillcolor("purple")
t1.begin_fill()
t1.seth(135)
t1.forward(100)
t1.right(45)
t1.forward(100)
t1.right(45)
t1.forward(100)
t1.right(45)
t1.forward(100)
t1.right(45)
t1.forward(100)
t1.right(45)
t1.forward(100)
t1.right(45)
t1.forward(100)
t1.right(45)
t1.forward(100)
t1.end_fill()
t1.hideturtle()

turtle.done()