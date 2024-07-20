import sys
import pygame
from pygame.locals import *

pygame.init()

DISPLAY = pygame.display.set_mode((1000, 1000), 0, 32)

GRAY = (150, 150, 150)
BLUE = (89, 121, 217)
AFTER_CLICK = (200, 200, 200)

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

get_all_button = pygame.Surface((500, 50), pygame.SRCALPHA)
get_all_button.fill(BLUE)

get_country_button = pygame.Surface((500, 50), pygame.SRCALPHA)
get_country_button.fill(BLUE)

insert_button = pygame.Surface((500, 50), pygame.SRCALPHA)
insert_button.fill(BLUE)

update_button = pygame.Surface((500, 50), pygame.SRCALPHA)
update_button.fill(BLUE)

delete_button = pygame.Surface((500, 50), pygame.SRCALPHA)
delete_button.fill(BLUE)

exit_button = pygame.Surface((500, 50), pygame.SRCALPHA)
exit_button.fill(BLUE)


def determine_mouseover(valx, valy, rectangle):
    if rectangle.collidepoint(valx, valy):
        return True
    else:
        return False


mouse_x, mouse_y = 0, 0

while True:
    DISPLAY.fill(GRAY)
    mouse_clicked = False
    DISPLAY.blit(get_all_button, rect.topleft)
    DISPLAY.blit(get_country_button, rect1.topleft)
    DISPLAY.blit(insert_button, rect2.topleft)
    DISPLAY.blit(update_button, rect3.topleft)
    DISPLAY.blit(delete_button, rect4.topleft)
    DISPLAY.blit(exit_button, rect5.topleft)

    rect = pygame.draw.rect(DISPLAY, BLUE, (200, 300, 500, 50))

    font = pygame.font.SysFont(None, 55)

    text = font.render('GET ALL COUNTRIES', True, (1, 1, 1))
    text_rect = text.get_rect()
    text_rect.topleft = (203, 310)
    DISPLAY.blit(text, text_rect)

    font1 = pygame.font.SysFont(None, 55)

    text1 = font.render('GET COUNTRY BY NAME', True, (1, 1, 1))
    text_rect1 = text1.get_rect()
    text_rect1.topleft = (206, 365)
    DISPLAY.blit(text1, text_rect1)

    font2 = pygame.font.SysFont(None, 55)

    text2 = font.render('INSERT COUNTRY', True, (1, 1, 1))
    text_rect2 = text2.get_rect()
    text_rect2.topleft = (206, 425)
    DISPLAY.blit(text2, text_rect2)

    font3 = pygame.font.SysFont(None, 55)

    text3 = font.render('UPDATE COUNTRY', True, (1, 1, 1))
    text_rect3 = text3.get_rect()
    text_rect3.topleft = (206, 485)
    DISPLAY.blit(text3, text_rect3)

    font4 = pygame.font.SysFont(None, 55)

    text4 = font.render('DELETE COUNTRY', True, (1, 1, 1))
    text_rect4 = text4.get_rect()
    text_rect4.topleft = (206, 545)
    DISPLAY.blit(text4, text_rect4)

    font5 = pygame.font.SysFont(None, 55)

    text5 = font.render('EXIT', True, (1, 1, 1))
    text_rect5 = text5.get_rect()
    text_rect5.topleft = (206, 605)
    DISPLAY.blit(text5, text_rect5)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
        elif event.type == MOUSEBUTTONUP:
            mouse_x, mouse_y = event.pos
            mouse_clicked = True

    mouseover_get_all = determine_mouseover(mouse_x, mouse_y, rect)

    if mouseover_get_all and not mouse_clicked:
        pygame.draw.rect(DISPLAY, AFTER_CLICK, rect, 3)
        if event.type == MOUSEBUTTONDOWN:
            print('radi')
            mouse_x, mouse_y = 0, 0

    mouseover_get_country = determine_mouseover(mouse_x, mouse_y, rect1)

    if mouseover_get_country and not mouse_clicked:
        pygame.draw.rect(DISPLAY, AFTER_CLICK, rect1, 3)
        if event.type == MOUSEBUTTONDOWN:
            print('radi')
            mouse_x, mouse_y = 0, 0

    mouseover_insert = determine_mouseover(mouse_x, mouse_y, rect2)

    if mouseover_insert and not mouse_clicked:
        pygame.draw.rect(DISPLAY, AFTER_CLICK, rect2, 3)
        if event.type == MOUSEBUTTONDOWN:
            print('radi')
            mouse_x, mouse_y = 0, 0

    mouseover_update = determine_mouseover(mouse_x, mouse_y, rect3)

    if mouseover_update and not mouse_clicked:
        pygame.draw.rect(DISPLAY, AFTER_CLICK, rect3, 3)
        if event.type == MOUSEBUTTONDOWN:
            print('radi')
            mouse_x, mouse_y = 0, 0

    mouseover_delete = determine_mouseover(mouse_x, mouse_y, rect4)

    if mouseover_delete and not mouse_clicked:
        pygame.draw.rect(DISPLAY, AFTER_CLICK, rect4, 3)
        if event.type == MOUSEBUTTONDOWN:
            print('radi')
            mouse_x, mouse_y = 0, 0

    mouseover_exit = determine_mouseover(mouse_x, mouse_y, rect5)

    if mouseover_exit and not mouse_clicked:
        pygame.draw.rect(DISPLAY, AFTER_CLICK, rect5, 3)
        if event.type == MOUSEBUTTONDOWN:
            print('radi')
            mouse_x, mouse_y = 0, 0


    pygame.display.update()
