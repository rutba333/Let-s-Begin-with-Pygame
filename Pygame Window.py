#Import necessary Libraries
import pygame
#Initialize required modules
pygame.init()
#setup window geometry
screen=pygame.display.set_mode((400,500))
#create a loop run until the game is quit by the user
done=False

while not done:
    #clear the event queue
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit

    #make the changes
    pygame.display.flip()
