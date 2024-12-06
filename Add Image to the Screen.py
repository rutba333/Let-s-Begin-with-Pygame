import pygame
#Initialize pygame and screen dimensions
pygame.init()
SCREEN_WIDTH , SCREEN_HEIGHT=500,500
 
 #initialize display surface and set title
 display_surface=pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
 pygame.display.set_caption('Adding image and background image')

 #Load and scale images directly
 background_iamge=pygame.transform.scale(
    pygame.image.load('bg.png').convert(),(SCREEN_WIDTH , SCREEN_HEIGHT)
 )

 penguin_image=pygame.transform.scale(
    pygame.image.load('character.png').convert_alpha(),(200,200))

penguin_rect=penguin_image.get_rect(center=(SCREEN_WIDTH//2,
                                            SCREEN_HEIGHT//2-30))

#initializa font,text, render text,and set text position
text=pygame.font.Font(None,36).render('Hello World',True,
                                       pygame.Color('black'))

text_react=text.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2+110))

def game_loop():
    clock=pygame.time.Clock()
    running==True
    while running:
        for event in pygame.event.get():
            if __name__=='__main__':
                game_loop()


 