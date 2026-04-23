import pygame
from pygame.locals import *

import random

pygame.init() 

size = width, height = (1000, 600)
road_width = int(width / 1.6)
roadmark_width = int(width / 80)

right_lane = width/2 + road_width/4
left_lane = width/2 - road_width/4

screen = pygame.display.set_mode(size)

#uses RGB value to give us a grassy green background
screen.fill((60, 220, 0))

pygame.display.set_caption("GWC x Game Dev Club's Video Game!")

#actually updates our game
pygame.display.update()

#load player image
car = pygame.image.load("car.png")

#load enemy image
car_enemy = pygame.image.load("otherCar.png")

# fetch the location of the images
car_location = car.get_rect()
car_enemy_location = car_enemy.get_rect()

#places the center of the cars in the correct lane
# player car will be on the bottom of the right lane
car_location.center = right_lane, height * 0.8 #x, y coords

# enemy car will be on the top of the left lane
car_enemy_location.center = left_lane, height*0.2


running = True

#game loop
while(running): 
    car_enemy_location[1] += 1

    if(car_enemy_location[1] > height):
        #if 0 is chosen as the random number...
        if (random.randint(0, 1) == 0):
            #the enemy moves to the right lane
            car_enemy_location.center = right_lane, -200
        
        #if 1 is chosen as the random number...
        else:
            #the enemy moves to the left lane
            car_enemy_location.center = left_lane, -200

    #if the cars are in the same lane AND the enemy car hits the front of the player...
    if (car_location[0] == car_enemy_location[0]) and (car_enemy_location[1] > car_location[1] - 250):
        print("GAME OVER!")
        break #break out of game loop
    

    for event in pygame.event.get():
        #quit event
        if (event.type == QUIT):
            running = False

        #selects ALL keys on our keyboard
        if (event.type == KEYDOWN):
            #if the key pressed is either the a key or left arrow key...
            if(event.key in [K_a, K_LEFT]):
                #moves the player to the left lane
                car_location = car_location.move([-int(road_width/2), 0]) #x, y coords

            if(event.key in [K_d, K_RIGHT]):
                car_location = car_location.move([int(road_width/2), 0])


    pygame.draw.rect(
        screen, 
        (50, 50, 50), #color of road
        (width/2 - road_width/2, 0, road_width, height) #x, y, width, height
    )

    pygame.draw.rect(
        screen, 
        (255, 240, 60),
        (width/2 - roadmark_width/2, 0, roadmark_width, height)
    )

    #leftmost line
    pygame.draw.rect(
        screen, 
        (255, 255, 255),
        ((width/2 - road_width/2) + roadmark_width*2, 0, roadmark_width, height)
    )

    #rightmost line
    pygame.draw.rect(
        screen, 
        (255, 255, 255),
        ((width/2 + road_width/2) - roadmark_width*3, 0, roadmark_width, height)
    )



    screen.blit(car, car_location)
    screen.blit(car_enemy, car_enemy_location)

    #update our game again now that we have a new drawing
    pygame.display.update()
    
pygame.quit() 


