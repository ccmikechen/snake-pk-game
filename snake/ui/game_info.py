from snake.entity import Entity
from snake.game_helper import show_text

WHITE = (255, 255, 255)

class GameInfo(Entity):
    def __init__(self, bound):
        self.bound = bound

    def update(self, delta, params):
        self.score_1 = params["score_1"]
        self.score_2 = params["score_2"]

    def render(self, screen):
        show_text(
            screen,
            "Player 1 score: " + str(self.score_1),
            WHITE,
            30,
            (20, 20)
        )
        show_text(
            screen,
            "Player 2 score: " + str(self.score_2),
            WHITE,
            30,
            (self.bound[0] - 20, 20),
            align_hor="right"
        )
