import pygame
from snake.scene import Scene
from snake.ui.information import Information

class MenuScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.information_ui = Information("Menu")

    def update(self):
        self.information_ui.update()

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.information_ui.render(screen)

    def on_key_down(self, key):
        if key == pygame.K_SPACE:
            self.start_scene("test")
