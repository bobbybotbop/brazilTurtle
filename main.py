import turtle

t = turtle.Turtle() 
t.speed(0)
num1 = 3
num2 = 14
number1 = 16
number2 = 1

def drawRectangle():
  t.penup()
  t.goto(-300, 150)

  t.color('green')
  t.pendown()
  t.begin_fill()
  for i in range(2):
    t.forward(500)
    t.right(90)
    t.forward(300)
    t.right(90)
  t.end_fill()
  t.penup()

def drawDiamond():
  global dia

  t.penup()
  t.rt(90)
  t.fd(150)
  t.lt(90)
  t.fd(50)
  t.color('yellow')
  t.pendown()
  t.begin_fill()
  t.lt(33)
  t.fd(238)
  t.rt(66)
  t.fd(238)
  t.penup()
  t.goto(-250,0)
  t.pendown()
  t.fd(238)
  t.lt(66)
  t.fd(238)
  t.end_fill()
  t.penup()
  t.rt(33)
    
def drawCircle():
  t.color('navy')
  t.penup()
  t.goto(-50,-80)
  t.pendown()
  t.begin_fill()
  t.circle(80)
  t.end_fill()
  t.penup()

def drawBand():
  global num1
  global num2
  global number1
  global number2
  
  t.penup()
  t.color('white')
  t.goto(-120,38)
  t.pendown()
  t.begin_fill()
  for i in range (4):
    for i in range(num1):
      t.fd(num2)
      t.rt(90)
      t.fd(1)
      t.lt(90)
    num1 += 1
    num2 -= 4

  for i in range (4):
    t.fd(-num2)
    t.rt(90)
    t.fd(1)
    t.lt(90)
  for i in range (10):
    t.fd(2)
    t.rt(90)
    t.fd(-num2)
    t.lt(90)

  t.penup()
  t.goto(-120,38)
  t.pendown()
  t.rt(90)
  for i in range (5):
    
    t.fd(4)
    t.rt(90)
    t.fd(3)
    t.lt(90)



  t.lt(90)


  t.goto(-135, 18)


  num1 = 3
  num2 = 14
  number1 = 16
  number2 = 1

  for i in range (4):
    for i in range(num1):
      t.fd(num2)
      t.rt(90)
      t.fd(1)
      t.lt(90)
    num1 += 1
    num2 -= 4

  for i in range (4):
    t.fd(-num2)
    t.rt(90)
    t.fd(1)
    t.lt(90)
  for i in range (15):
    t.fd(2)
    t.rt(90)
    t.fd(-num2)
    t.lt(90)

  t.lt(90)
  for i in range (5):
    
    t.fd(6)
    t.rt(90)
    t.fd(1)
    t.lt(90)

  t.end_fill()


    

drawRectangle()
drawDiamond()
drawCircle()
drawBand()