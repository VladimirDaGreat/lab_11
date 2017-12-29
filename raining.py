"""
 Pygame base template for opening a window

 a simple edit
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame, random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (176,224,230)
GAINSBORO = (220,220,220)
GREY = (128,128,128)
GOLD = (255,215,0)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# list for drawing rain
rain_list = []
for i in range(100):
    x = random.randrange(0, 700)
    y = random.randrange(0, 500)
    rain_list.append([x, y])
         
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(LIGHTBLUE)
 
    # --- Drawing code should go here

    # Draw path for character
    def draw_path():

        # Main rectangle
        pygame.draw.rect(screen, GREEN, [0, 400, 700, 100])

        # concrete
        pygame.draw.rect(screen, GREY, [0, 400, 700, 20])

    # Draws the flag from mario ending
    def draw_flag():

        # Pole
        pygame.draw.rect(screen, GAINSBORO, [600, 150, 5, 250])

        # Flag
        pygame.draw.rect(screen, WHITE,  [550, 150, 50, 50])
        pygame.draw.circle(screen, RED, [575, 175], 15)
        

    draw_path()
    draw_flag()
        

    # Process each rain drop in the list
    for i in range(len(rain_list)):

        # Draw the rain drop
        pygame.draw.rect(screen, BLUE, [rain_list[i][0],rain_list[i][1], 2, 10])

        # Move the rain droplet down one pixel
        rain_list[i][1] += 8

        # If the rain drop has moved off the bottom of the screen
        if rain_list[i][1] > 400:
            # Reset it just aboce the top
            y = random.randrange(-50, -10)
            rain_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 700)
            rain_list[i][0] = x
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

    print(rain_list)
 
# Close the window and quit.
pygame.quit()
