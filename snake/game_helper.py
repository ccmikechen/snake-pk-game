import pygame

def show_text(screen, text, color, size, position):
    font = pygame.font.SysFont('Noto Sans CJK SC', size)
    string = font.render(text, 1, color)
    screen.blit(string, position)
