import pgzrun
import random

WIDTH = 500
HEIGHT = 500

bee = Actor('bee')
bee.pos = (400,100)
flower = Actor('flower')
flower.pos = (150,300)

score = 0

def draw():
    screen.clear()
    flower.draw()
    bee.draw()
    screen.draw.text('score:' + str(score) ,center = (50,10), fontsize = 30 )


def place():
    flower.x = random.randint(0,WIDTH)
    flower.y = random.randint(0,HEIGHT)

  
def update():
    global score
    if keyboard.left:
        bee.x = bee.x - 2
    if keyboard.right:
        bee.x = bee.x + 2
    if keyboard.up:
        bee.y = bee.y - 2
    if keyboard.down:
        bee.y = bee.y + 2
    if bee.colliderect(flower):
        score = score + 10
        place()


pgzrun.go()