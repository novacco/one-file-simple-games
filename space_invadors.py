import turtle
import os
import math
import random

#set up the screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders")
win.bgpic("space_invaders_background.gif")

#register the shapes of turtles
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create player's turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setheading(90)
player.setposition(0, -250)



score = 0
#draw score

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring  = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#define bullet state
#ready to fire
#fire - is firing

bulletstate = "ready"

###   moving the turtle ---->
playerspeed = 15 # distance of the player's move

# left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if not bullet.isvisible():
        os.system("aplay laser.wav&")
        #move the bullet above the player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x,y + 10)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else: 
        return False


# keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#choose the number of enemies
number_of_enemies = 8

#list of enemies
enemies = []

#add enemies to the list

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100, 250)
    enemy.setposition(x,y)

enemyspeed = 6 #here u can change the enemy's speed

### main game loop :D
while True:
    
    for enemy in enemies:
        #move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #move the enemy back and down
        if enemy.xcor() > 280:
            #all enemies down 
            for e in enemies: #e as enemy
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1 #direction

        if enemy.xcor() < -280:
            for e in enemies: #e as enemy 
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1 #direction

        #check for collision
        if isCollision(bullet, enemy):
            #play explosion
            os.system("aplay explosion.wav&")
            #add score
            score+=10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            score_pen.hideturtle()
            #reset bullet
            bullet.hideturtle()
            bullet.setposition(0, -400)
            #reset enemy
            x = random.randint(-200,200)
            y = random.randint(100, 250)
            enemy.setposition(x,y)
        
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game over btch")
            break

    #move the bullet
    if bullet.isvisible():
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    
    #bullet reach the top???
    if bullet.ycor() > 275:
        bullet.hideturtle()


#delay = input("Press sth")
