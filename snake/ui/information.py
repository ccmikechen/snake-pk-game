from snake.entity import Entity
from snake.game_helper import show_text

WHITE = (255, 255, 255)

class Information(Entity):
    def update(self, delta):
        pass

    def render(self, screen):
        show_text(screen, 'Snake Game', WHITE, 100, (250, 150))
        show_text(screen, 'press SPACE to start', WHITE, 40, (250, 350))
        show_text(screen, 'Player 1 - A = turn left, D = turn right', WHITE, 30, (250, 450))
        show_text(screen, 'Player 2 - J = turn left, L = turn right', WHITE, 30, (250, 550))
