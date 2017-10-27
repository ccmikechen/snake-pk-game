from snake.entity import Entity
from snake.ui.snake import Snake

class Player(Entity):
    def __init__(self, scene, position, color):
        self.snake = Snake(scene.get_bound(), position)
        self.snake.set_speed(300)
        self.snake.set_color(color)
        self.is_turning_right = False
        self.is_turning_left = False

    def add_snake_length(self, delta):
        self.snake.add_length(delta)

    def update(self, delta):
        if self.is_turning_right:
            self.snake.add_direction(360 * delta)
        if self.is_turning_left:
            self.snake.add_direction(-360 * delta)

        self.snake.update(delta)

    def render(self, screen):
        self.snake.render(screen)
