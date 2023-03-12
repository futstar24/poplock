import turtle
import random

screen = turtle.Screen()
screen.setup(1.0,1.0)

score = 0
r = 150

rect = turtle.Turtle()
rect.shape("square")

scoreT = turtle.Turtle()
text = "Score: " + str(score)
scoreT.penup()
scoreT.ht()
scoreT.write(text,align = "center",font = ["Arial",20])

coin = turtle.Turtle()
coin.shape("circle")
coin.color("yellow")
coin.penup()
coin.speed(0)
coin.sety(r * -1)
coin.shapesize(3)
num = random.randint(75,150)
coin.circle(r,num)

def flip(x,y):
  global speedy
  global score
  global coin
  global rect
  global gameOver
  global waiting
  if coin.distance(rect) < 40:
    waiting = False
    score += 1
    scoreT.clear() 
    text = "Score: " + str(score)
    scoreT.write(text,align = "center",font = ["Arial",20])
    speedy *= -1
    close = [50,80]
    mid = [80,120]
    far = [120,150]
    chances = {20:{"close":[0],"mid":[1,2,3,4],"far":[5,6,7,8,9]},25:{"close":[0,1],"mid":[2,3,4,5,6],"far":[7,8,9]},30:{"close":[0,1,2,3,4],"mid":[5,6,7,8,9],"far":[]},35:{"close":[0,1,2,3,4,5,6],"mid":[7,8,9],"far":[]},40:{"close":[],"mid":[],"far":[0,1,2,3,4,5,6,7,8,9]}}
    rand = random.randint(0,9)
    speedTemp = abs(speedy)
    if rand in chances[speedTemp]["close"]:
      num = random.randint(close[0],close[1])
    elif rand in chances[speedTemp]["mid"]:
      num = random.randint(mid[0],mid[1])
    else:
      num = random.randint(far[0],far[1])
    if speedy < 0:
      num *= -1
    coin.circle(r,num)
  else:
    gameOver = True

rect.penup()
rect.speed(10)
rect.sety(r*-1)

turtle.onscreenclick(flip)

speedy = 20
gameOver = False
change = True
waiting = False
while not gameOver:
  rect.circle(r,speedy)
  if score % 12 == 0 and score != 0 and change:
    speedy += 5
    change = False
  elif score % 12 != 0:
    change = True
  if coin.distance(rect) < 40:
    waiting = True
  if waiting and coin.distance(rect) > 40:
    gameOver = True
  if score == 49:
    gameOver = True

if score == 49:
  scoreT.clear() 
  text = "You WIN... \n https://docs.google.com/document/d/1m-clZMxgidOH3cdOOuCUQFPvwUxUl2RwJ2EZYfYcTFI/edit?usp=sharing"
  scoreT.write(text,align = "center",font = ["Arial",20])
  
else:
  scoreT.clear() 
  text = "You Lose!"
  scoreT.write(text,align = "center",font = ["Arial",20])
