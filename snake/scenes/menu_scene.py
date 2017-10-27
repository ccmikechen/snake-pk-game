import pygame
from snake.resource import R
from snake.scene import Scene
from snake.ui.information import Information

class MenuScene(Scene):
    def setup(self):
        self.information_ui = Information()
        R.play_music("menu")

    def update(self, delta):
        self.information_ui.update(delta)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.information_ui.render(screen)

    def on_key_down(self, key):
        if key == pygame.K_SPACE:
            R.get_sound("enter").play()
            self.start_and_reset_scene("game")
