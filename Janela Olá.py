import pygame
screen = pygame.display.set_mode((800, 600))
pygame.font.init()
font1 = pygame.font.Font(None, 90)
text = font1.render("Oi, Sou o PyGame", True, (255, 255, 255))
screen.blit(text, (0, 200))
pygame.display.flip()

def principal():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return
        pygame.time.delay(30)

principal() 