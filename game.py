from random import randint
import pgzrun

WIDTH = 800
HEIGHT = 600

balloon = Actor("balloon")
balloon.pos = (400, 300)

bird = Actor("bird-up")
bird.pos = (randint(800, 1600), randint(10, 200))

house = Actor("house")
house.pos = (randint(800, 1600), 460)

tree = Actor("tree")
tree.pos = (randint(800, 1600), 450)

bird_up = True
up = False
game_over = False
score = 0
number_of_updates = 0

scores = []

def update_high_scores():
    pass

def display_high_scores():
    pass

def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird_up = True

def on_mouse_down():
    global up
    up = True
    balloon.y -= 50

def on_mouse_up():
    global up
    up = False

def draw():
    screen.blit("background", (0, 0))
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text("Score: " + str(score), (700, 5), color="black")
    else:
        display_high_scores()

def update():
    global game_over, score, number_of_updates

    if not game_over:
        if not up:
            balloon.y += 1

        if bird.x > 0:
            bird.x -= 4
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        else:
            bird.x = randint(800, 1600)
            bird.y = randint(10, 200)
            score += 1
            number_of_updates = 0
        
        if house.x > 0:
            house.x -= 2
        else:
            house.x = randint(800, 1600)
            score += 1

        if tree.x > 0:
            tree.x -= 2
        else:
            tree.x = randint(800, 1600)
            score += 1

        if balloon.y < 0 or balloon.y > 560:
            game_over = True
            update_high_scores()

        if balloon.collidepoint(bird.x, bird.y) or \
            balloon.collidepoint(house.x, house.y) or \
            balloon.collidepoint(tree.x, tree.y):
            game_over = True
            update_high_scores()

pgzrun.go()
