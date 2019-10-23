import turtle
y = turtle.Pen()
x = turtle.Pen()
x.shape("circle")
x.color("maroon")
x.speed(0)
y.shape("circle")
y.speed(0)
y.width(5)
x.width(5)
x.backward(500)
y.backward(500)
y.color("blue")
z = turtle.Pen()
z.shape("circle")
z.color("purple")
z.backward(500)
z.speed(0)

turtle.bgcolor("black")

for i in range(150):
    y.forward(250)
    y.right(95)
    y.circle(4)
    y.right(90)
    y.backward(1050)
    
for i in range(150):
    z.forward(50)
    z.width(5)
    z.right(95)
    z.circle(4)
    z.right(90)
    z.width(2)
    z.backward(1250)
    
for i in range(150):
    x.forward(150)
    x.width(5)
    x.right(95)
    x.circle(4)
    x.right(90)
    x.width(2)
    x.backward(1150)
    

x.color("black")

    
    


