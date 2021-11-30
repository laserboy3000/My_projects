##################################
# Autor: Voitov Vladimir         #
# Date: 29.11.21                 #
# Task: Home Work to  L7(pygame) #
##################################



def game_1():
    import pygame
    run = True
    width = 400
    height = 100
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    font = pygame.font.SysFont(None, 48)
    text = font.render('Welcome to pygame', True, (255, 255, 255))
    screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()*1.75)))
    # up str добавил скобочек и пришлось на 1,75 умножить, дабы отцентрировать
    pygame.display.flip()
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT\
            or event.type == pygame.MOUSEBUTTONUP\
            or event.type == pygame.KEYUP:
                run = False
game_1()
