
import pygame     #game inported, all varibles in higher case
from time import sleep
import random
pygame.init()

BACKGROUND_COLOUR = 255, 255, 255    #bg varible
WIDTH, HEIGHT = 900, 500       #dimensions varible
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))   #telling the program to make a new window with that varible


SCREEN.fill(BACKGROUND_COLOUR)       #telling the program to change to the bg varible 

FPS = 10   #pretty self explanitory    #for movement

def main():
    run = True
    VEL = 0
    x, y = 250, 450
    CHAR = pygame.Surface((25, 25))#pygame.image.load("square.png")        #Just load the image once here
    BLIP = pygame.Surface((5, 5))
    blip_exists = False
    blips_colc = 0
    def title(blips_colc):
        pygame.display.set_caption(f"blip quest! BLIPS: {blips_colc}")     #window name
    title(blips_colc)
    
    
    while run:
        pygame.time.delay(100)          #wait function from scratch
        SCREEN.fill(BACKGROUND_COLOUR)

        def character():
            SCREEN.blit(CHAR, (x, y))    #position (from top left corner)

        def blip(blip_loc_x, blip_loc_y):
            SCREEN.blit (BLIP, (blip_loc_x, blip_loc_y))

        character()
        if blip_exists == True:
            blip(blip_loc_x, blip_loc_y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:       #so you can actually close it
                run = False
        keys_pressed = pygame.key.get_pressed()
        
        #Jumping?
        if keys_pressed[pygame.K_w]:
            if y > 0:
                y -= 10
            print(x, y)
        if keys_pressed[pygame.K_s]:
            if y < 470:
                y += 10
            print(x, y)

        if keys_pressed[pygame.K_a]:
            if x > 0:
                x -= 10
            print(x, y)      #print commands to check if movenent works
        if keys_pressed[pygame.K_d]:
            if x < 870:
                x += 10
            print(x, y)

        if blip_exists == False:

            blip_loc_x = random.randint(1, 860)
            blip_loc_y = random.randint(1,460)
            blip(blip_loc_x, blip_loc_y)
            print(blip_loc_x, blip_loc_y)
            blip_exists = True

        #Wonky formula to calculate the distance to the Blip.

        difference_x = x - blip_loc_x
        if difference_x < 0:
            difference_x = difference_x - difference_x - difference_x
        difference_y = y - blip_loc_y
        if difference_y < 0:
            difference_y = difference_y - difference_y - difference_y


        if difference_x < 15 and difference_y < 15:
            print('yay!')
            blip_exists = False
            blips_colc +=1
            title(blips_colc)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":         #Runs main
    main()


























#import turtle
#import os
#import random
#
#w = 500
#h = 500
#food_size = 10
#delay = 100
# 
#offsets = {
#    "up": (0, 20),
#    "down": (0, -20),
#    "left": (-20, 0),
#    "right": (20, 0)
#}
# 
#def reset():
#    global snake, snake_dir, food_position, pen
#    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
#    snake_dir = "up"
#    food_position = get_random_food_position()
#    food.goto(food_position)
#    move_snake()
#     
#def move_snake():
#    global snake_dir
# 
#    new_head = snake[-1].copy()
#    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
#    new_head[1] = snake[-1][1] + offsets[snake_dir][1]
# 
#     
#    if new_head in snake[:-1]:
#        reset()
#    else:
#        snake.append(new_head)
# 
#     
#        if not food_collision():
#            snake.pop(0)
# 
# 
#        if snake[-1][0] > w / 2:
#            snake[-1][0] -= w
#        elif snake[-1][0] < - w / 2:
#            snake[-1][0] += w
#        elif snake[-1][1] > h / 2:
#            snake[-1][1] -= h
#        elif snake[-1][1] < -h / 2:
#            snake[-1][1] += h
# 
# 
#        pen.clearstamps()
# 
#         
#        for segment in snake:
#            pen.goto(segment[0], segment[1])
#            pen.stamp()
# 
#         
#        screen.update()
# 
#        turtle.ontimer(move_snake, delay)
# 
#def food_collision():
#    global food_position
#    if get_distance(snake[-1], food_position) < 20:
#        food_position = get_random_food_position()
#        food.goto(food_position)
#        return True
#    return False
# 
#def get_random_food_position():
#    x = random.randint(- w / 2 + food_size, w / 2 - food_size)
#    y = random.randint(- h / 2 + food_size, h / 2 - food_size)
#    return (x, y)
# 
#def get_distance(pos1, pos2):
#    x1, y1 = pos1
#    x2, y2 = pos2
#    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
#    return distance
#def go_up():
#    global snake_dir
#    if snake_dir != "down":
#        snake_dir = "up"
# 
#def go_right():
#    global snake_dir
#    if snake_dir != "left":
#        snake_dir = "right"
# 
#def go_down():
#    global snake_dir
#    if snake_dir!= "up":
#        snake_dir = "down"
# 
#def go_left():
#    global snake_dir
#    if snake_dir != "right":
#        snake_dir = "left"
# 
# 
#screen = turtle.Screen()
#screen.setup(w, h)
#screen.title("Snake")
#screen.bgcolor("red")
#screen.setup(500, 500)
#screen.tracer(0)
# 
# 
#pen = turtle.Turtle("square")
#pen.penup()
# 
# 
#food = turtle.Turtle()
#food.shape("square")
#food.color("yellow")
#food.shapesize(food_size / 40)
#food.penup()
# 
# 
#screen.listen()
#screen.onkey(go_up, "Up")
#screen.onkey(go_right, "Right")
#screen.onkey(go_down, "Down")
#screen.onkey(go_left, "Left")
# 
# 
#reset()
#turtle.done()