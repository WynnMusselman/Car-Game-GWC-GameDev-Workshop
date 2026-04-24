"""
mod ideas:
- create your own assets for the cars
- make it so the car can not drive off side of road
- increase enemy's speed as game progresses
- add score 
"""

#https://www.youtube.com/watch?v=W-QOtdD3qx4

import pygame #pip install pygame
import random # python -m pygame.examples.aliens

#initialize pygame app
pygame.init()
pygame.font.init() #for score mod

#allows us to use relative sizing instead of absolute
size = width, height = (1000, 600) #even if we change these numnbers, the graphics in the game will adjust accordingly
road_width = width // 1.6
roadmark_width = width // 80
right_lane = width/2 + road_width/4
left_lane = width/2 - road_width/4
speed = 1

score = 0

#window size is 1000 x 600
screen = pygame.display.set_mode(size)
#background color in RGB
screen.fill((60, 220, 0))
pygame.display.set_caption ("GWC x GAME DEV CAR GAME!")

pygame.display.update() #now our screen actually updates!

#loads player image
car = pygame.image.load("car.png") #very simple mod idea - draw your own images and insert it into the game :)
car_location = car.get_rect()
# places car in the right lane at bottom
car_location.center = right_lane, height*0.8

#loads enemy image
car_enemy = pygame.image.load("otherCar.png")
car_enemy_location = car_enemy.get_rect()
# places car in the left lane at top
car_enemy_location.center = left_lane, height*0.2


counter = 0 #used for mod where enemy's speed increases 

#mod - show score at top of screen
font = pygame.font.Font(None, 36)

running = True
right_side = True
while running:
    screen.fill((60, 220, 0)) #repaints the background everytime since graphics are being drawn overtop, necessary for score mod

    #mod - increase enemy's speed as game progresses
    counter += 1
    if (counter == 1024):
        speed += 0.25
        counter = 0
        print("Level Up!", speed)


    #animate enemy vehicle
    #car_enemy_location[0] = x coord
    #car_enemy_location[1] = y coord
    car_enemy_location[1] += speed
    if(car_enemy_location[1] > height):        
        #places enemy in right or left lane randomly
        if(random.randint(0, 1) == 0): 
            car_enemy_location.center = right_lane, -200
        else:
            car_enemy_location.center = left_lane, -200

    #end game
    #if vehicles collide
    if(car_location[0] == car_enemy_location[0]) and (car_enemy_location[1] > car_location[1] - 250):
        print("GAME OVER")
        break #breaks while loop to bring game to very last line of code, which collapses game window

    #for score mod, if the player passes an enemy, the score increases
    #if the cars are not in the same lane, but the have the same height, increase speed by 1
    if (car_location[0] != car_enemy_location[0]) and (car_enemy_location[1] == car_location[1] - 250):
        score += 1
        print(score)

    #all events are stored in pygame.event
    for event in pygame.event.get():
        if (event.type == pygame.QUIT): #x button DOES NOT WORK without this
            running = False

        #mod idea - make it so the car can not move outside of the road. 
        # control player car
        if(event.type == pygame.KEYDOWN):
            # if player clicks a or left arrow key, move left
            if(event.key in [pygame.K_a, pygame.K_LEFT]) and (right_side == True): 
                car_location = car_location.move([-road_width//2, 0]) #[x, y]
                right_side = False #car is no longer on right side of road
            #move right
            if(event.key in [pygame.K_d, pygame.K_RIGHT]) and (right_side == False):
                car_location = car_location.move([road_width//2, 0]) #[x, y]
                right_side = True #car is now on right side of road


    #GRAPHICS 
 
    # graphics of road
    pygame.draw.rect(
        screen, #surface
        (50, 50, 50), #color
        #centers road
        (width/2 - road_width/2, 0, road_width, height) #coordinates and size
    )

    # road marking graphics
    pygame.draw.rect(
        screen, 
        (255, 240, 60),
        (width/2 - roadmark_width / 2, 0, roadmark_width, height)
    )

    # white line at edge of road graphics
    pygame.draw.rect(
        screen, 
        (255, 255, 255),
        #line is drawn 20px from edge of road
        (width/2 - road_width / 2 + roadmark_width * 3, 0, roadmark_width, height)
    )

    # other white line at edge of road graphics
    pygame.draw.rect(
        screen, 
        (255, 255, 255),
        (width/2 + road_width / 2 - roadmark_width * 3, 0, roadmark_width, height)
    )


    #blit is like a draw operation
    #blit = block image transfer, draws pixels of one image onto another
    screen.blit(car, car_location)
    screen.blit(car_enemy, car_enemy_location)

    #draws score for mod
    score_text = font.render(f'Score: {int(score)}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update() #update our game again!

#collapse app window
pygame.quit()