import pygame
from snake.scene import Scene
from snake.ui.player import Player

BLUE = (0, 0, 255)
RED = (255, 0, 0)

class GameScene(Scene):
    def setup(self):
        self.player_1 = Player(self, (100, 100), BLUE)
        self.player_2 = Player(self, (300, 100), RED)

    def update(self, delta):
        self.player_1.update(delta)
        self.player_2.update(delta)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.player_1.render(screen)
        self.player_2.render(screen)

    def on_key_down(self, key):
        if key == pygame.K_z:
            self.player_1.add_snake_length(10)
        if key == pygame.K_x:
            self.player_2.add_snake_length(10)
        if key == pygame.K_d:
            self.player_1.is_turning_right = True
        if key == pygame.K_a:
            self.player_1.is_turning_left = True
        if key == pygame.K_l:
            self.player_2.is_turning_right = True
        if key == pygame.K_j:
            self.player_2.is_turning_left = True

    def on_key_up(self, key):
        if key == pygame.K_d:
            self.player_1.is_turning_right = False
        if key == pygame.K_a:
            self.player_1.is_turning_left = False
        if key == pygame.K_l:
            self.player_2.is_turning_right = False
        if key == pygame.K_j:
            self.player_2.is_turning_left = False
