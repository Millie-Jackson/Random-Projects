''' RESOURCES
Playlist Tutorial: https://www.youtube.com/watch?v=MMxFDaIOHsE&list=PLzMcBGfZo4-lwGZWXz5Qgta_YNX3_vLS2&index=1&t=0s
Sprites: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqay1DZzUzTEtZdlFjUlBHZGJoRE5lb3QxWGdDUXxBQ3Jtc0tuLWo0TnFGZDFxajRBZzVHdlNWTXRIM3ZyMUZCZk1zWjhKaXlCTHJFMjhsWXI3bWpYdWFWQjRhN3hjaGF2MWhwUHpFc2VoYm5iZFoyTU1ITGNMb3B2cnlqLUtJRVJMR2s3NnlMeEJUaVpwd3UyZkoyOA&q=https%3A%2F%2Ftechwithtim.net%2Fwp-content%2Fuploads%2F2019%2F08%2Fimgs.zip&v=MMxFDaIOHsE
'''

import pygame
import neat
import time
import os
import random

# Window size
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800

# Load all the images into a list
# scale2x = makes each image twice as big
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))), 
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))), 
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25 # How much the bdraw_window(window, bird) ird needs to tilt
    ROTATION_VELOCITY = 20 # How much to rotate each frame
    ANIMATION_TIME = 5 # How long to display each animation

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.velocity = 0
        self.height = self.y
        self.img_count = 0 # Current image showing
        self.img = self.IMGS[0]

    def jump(self):
        self.velocity = -10.5 # Move up must be a negative number from current
        self.tick_count = 0 # Reset to 0 to keep track of when we last jumped
        self.height = self.y # WHere the bird started to jump from

    def move(self):
        self.tick_count += 1 # How many moves we have made since the last jump

        # -10.5 + 1.5 = -9 Moving 9 pixels up 
        displacement = self.velocity*self.tick_count + 1.5*self.tick_count**2 # How much the bird has moved up or down  

        # TERMINAL VELOCITY
        # Failsafe = not too heigh or low
        if displacement >= 16:
            displacement = 16
        
        if displacement < 0:
            displacement -= 2
    
        # Move slowly up or down
        self.y = self.y + displacement

        # ROTATION
        # Tilt upwards
        if displacement < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION: # Dont tilt it too far
                self.tilt = self.MAX_ROTATION
            else: # Tilt downwards
                if self.tilt > -90:
                    self.tilt -= self.ROTATION_VELOCITY

    def draw(self, window):
        self.img_count += 1 # How long an image has been displayed for

        # ANIMATION
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMG[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMG[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMG[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMG[1]
        elif self.img_count < self.ANIMATION_TIME*4 + 1:
            self.img = self.IMG[0]
            self.img_count = 0 # Reset

        # Stop bird from flapping when diving
        if self <= - 80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2 # Make sure it doesnt skip an animation frame
        
        # Rotate the image
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        # Around the center instead of the defaul 0,0 corner
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        window.blit(rotated_image, new_rect.topleft) # blit = draw

    # GET COLLISION
    def get_mask(self):
        return pygame.mask.from_surface(self.img)
    
def draw_window(window, bird):
    # blit = draw
    window.blit(BG_IMG, (0, 0)) # 0, 0 = top left
    bird.draw(window)
    # Refresh
    pygame.display.update()

def main():
    # Make a bird
    bird = Bird(200, 200)
    # Make a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    run = True
    while run:
        # If something happens
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        
        bird.move()
        draw_window(window, bird) 

    #pygame.quit()
    #quit()

main()