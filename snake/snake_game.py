import pygame
from snake.game import Game
from snake.scenes.menu_scene import MenuScene
from snake.scenes.test_scene import TestScene

class SnakeGame(Game):
    def __init__(self):
        super().__init__(title='Snake',
                         window_size=(1440, 960),
                         fps=10)

        self.register_scene(MenuScene, "menu")
        self.register_scene(TestScene, "test")

    def start(self):
        self.current_scene = self.scenes_manager.get_scene_by_name("menu")
        super().start()
