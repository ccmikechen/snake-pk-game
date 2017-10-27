from snake.entity import Entity
from snake.game_helper import show_text

WHITE = (255, 255, 255)

class Information(Entity):
    def __init__(self, name):
        self.name = name

    def update(self, delta, params):
        fps = int(params["fps"])
        self.name = str(fps)

    def render(self, screen):
        show_text(screen, '2017 KUAS 電腦遊戲設計實務', WHITE, 25, (50, 50))
        show_text(screen, '1103137124 ' + self.name, WHITE, 20, (50, 80))

    def change_name(self, name):
        self.name = name
