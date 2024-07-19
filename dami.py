import pygame
from pygame.locals import *


pygame.init()

DISPLAY = pygame.display.set_mode((1000, 1000), 0, 32)

GRAY = (150, 150, 150)
BLUE = (89, 121, 217)

DISPLAY.fill(GRAY)

rect = pygame.draw.rect(DISPLAY, BLUE, (200, 300, 500, 50))

font = pygame.font.SysFont(None, 55)

text = font.render('GET ALL COUNTRIES', True, (1, 1, 1))
text_rect = text.get_rect()
text_rect.topleft = (203, 310)
DISPLAY.blit(text, text_rect)

rect1 = pygame.draw.rect(DISPLAY, BLUE, (200, 360, 500, 50))

font1 = pygame.font.SysFont(None, 55)

text1 = font.render('GET COUNTRY BY NAME', True, (1, 1, 1))
text_rect1 = text1.get_rect()
text_rect1.topleft = (206, 365)
DISPLAY.blit(text1, text_rect1)

rect2 = pygame.draw.rect(DISPLAY, BLUE, (200, 420, 500, 50))

font2 = pygame.font.SysFont(None, 55)

text2 = font.render('INSERT COUNTRY', True, (1, 1, 1))
text_rect2 = text2.get_rect()
text_rect2.topleft = (206, 425)
DISPLAY.blit(text2, text_rect2)

rect3 = pygame.draw.rect(DISPLAY, BLUE, (200, 480, 500, 50))

font3 = pygame.font.SysFont(None, 55)

text3 = font.render('UPDATE COUNTRY', True, (1, 1, 1))
text_rect3 = text3.get_rect()
text_rect3.topleft = (206, 485)
DISPLAY.blit(text3, text_rect3)

rect4 = pygame.draw.rect(DISPLAY, BLUE, (200, 540, 500, 50))

font4 = pygame.font.SysFont(None, 55)

text4 = font.render('DELETE COUNTRY', True, (1, 1, 1))
text_rect4 = text4.get_rect()
text_rect4.topleft = (206, 545)
DISPLAY.blit(text4, text_rect4)


rect5 = pygame.draw.rect(DISPLAY, BLUE, (200, 600, 500, 50))

font5 = pygame.font.SysFont(None, 55)

text5 = font.render('EXIT', True, (1, 1, 1))
text_rect5 = text5.get_rect()
text_rect5.topleft = (206, 605)
DISPLAY.blit(text5, text_rect5)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.display.update()

