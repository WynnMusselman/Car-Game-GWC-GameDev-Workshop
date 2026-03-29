#https://www.youtube.com/watch?v=W-QOtdD3qx4

import pygame #python3 -m pip install -U pygame --user
import random

#initialize pygame app
pygame.init()
running = True

#allows us to use relative sizing instead of absolute
size = width, height = (1000, 600) #even if we change these numnbers, the graphics in the game will adjust accordingly
road_width = width // 1.6
roadmark_width = width // 80
right_lane = width/2 + road_width/4
left_lane = width/2 - road_width/4
speed = 1

#window size is 1000 x 600
screen = pygame.display.set_mode(size)
#background color in RGB
screen.fill((60, 220, 0))
pygame.display.set_caption ("GWC x GAME DEV CAR GAME!")

pygame.display.update() #now our screen actually updates!

#loads player image
car = pygame.image.load("car.png") 
car_location = car.get_rect()
# places car in the right lane at bottom
car_location.center = right_lane, height*0.8

#loads enemy image
car_enemy = pygame.image.load("otherCar.png")
car_enemy_location = car_enemy.get_rect()
# places car in the left lane at top
car_enemy_location.center = left_lane, height*0.2



#waits for user to click exit button and once they do so, exit app
while running:
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

    #all events are stored in pygame.event
    for event in pygame.event.get():
        if (event.type == pygame.QUIT): #x button DOES NOT WORK without this
            running = False

        #mod idea - make it so the car can not move outside of the road. this was not addressed in the video so below is how i thought to do it
        # control player car
        if(event.type == pygame.KEYDOWN):
            # if player clicks a or left arrow key, move left
            if(event.key in [pygame.K_a, pygame.K_LEFT]): 
                car_location = car_location.move([-road_width//2, 0]) #[x, y]
            #move right
            if(event.key in [pygame.K_d, pygame.K_RIGHT]):
                car_location = car_location.move([road_width//2, 0]) #[x, y]


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

    pygame.display.update() #update our game again!


#collapse app window
pygame.quit()