#кликер на питоне
import pygame
import random
from Constants import Constants
from Colours import Colours
from Player import Player            

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, Colours.WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
pygame.display.set_caption("кликер")
clock = pygame.time.Clock()
player = Player()
Constants.all_sprites.add(player)
timeofgame = 0
score = 0
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(Constants.FPS)
    timeofgame += 0.015
    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:#если нажимаем на лкм то очки растут
            score += 1
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    Constants.all_sprites.update()
    
    # Рендеринг
    screen.fill(Colours.BLACK)
    Constants.all_sprites.draw(screen)
    draw_text(screen, str(score), 30, Constants.WIDTH / 2, 10)#создаём тексты
    draw_text(screen,str( int(timeofgame)), 30, Constants.WIDTH - 27, Constants.HEIGHT - 30)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()