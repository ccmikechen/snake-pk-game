import pygame
from random import randint
from math import sqrt
from snake.scene import Scene
from snake.ui.player import Player
from snake.ui.food import Food
from snake.game_helper import show_text

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

GAME_OVER = "game_over"
DRAW = "draw"
CONTINUE = "continue"

MAX_FOODS = 10

class GameScene(Scene):
    def setup(self):
        self.reset()

    def reset(self):
        self.is_running = True
        self.game_status = None
        self.player_1 = Player(self, (100, 100), BLUE)
        self.player_1.add_snake_length(10)
        self.player_2 = Player(self, (300, 100), RED)
        self.player_2.add_snake_length(10)
        self.foods = []

    def get_game_status(self):
        player_1_collisions = self.count_collisions(self.player_1)
        player_2_collisions = self.count_collisions(self.player_2)

        if player_1_collisions > 5 or player_2_collisions > 5:
            if player_1_collisions > player_2_collisions:
                return GameStatus(GAME_OVER, self.player_2)
            elif player_1_collisions < player_2_collisions:
                return GameStatus(GAME_OVER, self.player_1)
            else:
                return GameStatus(DRAW)

        return GameStatus(CONTINUE)

    def count_collisions(self, player):
        collision_count = player.check_collision([self.player_1.snake, self.player_2.snake])

        return collision_count

    def generate_food(self):
        (x_bound, y_bound) = self.game.get_bound()
        x = randint(20, x_bound - 20)
        y = randint(20, y_bound - 20)
        self.foods.append(Food((x, y), 10))

    def check_eating_foods(self, player):
        for food in self.foods:
            if self.check_food_collision(player.snake, food):
                food.active(player.snake)
                self.foods.remove(food)

    def check_food_collision(self, snake, food):
        head = snake.body.get_head()
        distance = sqrt((head[0] - food.position[0])**2 + (head[1] - food.position[1])**2)
        print(distance)

        return distance < (snake.body.size + food.size)

    def update(self, delta):
        if self.is_running:
            if len(self.foods) < MAX_FOODS:
                self.generate_food()
            for food in self.foods:
                food.update(delta)

            self.player_1.update(delta)
            self.player_2.update(delta)
            self.check_eating_foods(self.player_1)
            self.check_eating_foods(self.player_2)

            self.game_status = self.get_game_status()

            if self.game_status.status != CONTINUE:
                self.is_running = False

    def render(self, screen):
        screen.fill((0, 0, 0))

        for food in self.foods:
            food.render(screen)

        self.player_1.render(screen)
        self.player_2.render(screen)

        if self.game_status != None:
            if self.game_status.status == GAME_OVER:
                self._show_winner_message(screen, self.game_status.winner)
            elif self.game_status.status == DRAW:
                self._show_draw_message(screen)

    def on_key_down(self, key):
        if key == pygame.K_SPACE:
            if not self.is_running:
                self.reset()
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

    def _show_winner_message(self, screen, winner):
        if winner == self.player_1:
            show_text(screen, "Player 1 win", BLUE, 50, (200, 200))
        elif winner == self.player_2:
            show_text(screen, "Player 2 win", RED, 50, (200, 200))

        show_text(screen, "press SPACE to continue", WHITE, 30, (200, 280))

    def _show_draw_message(self, screen):
        show_text(screen, "Draw", WHITE, 50, (200, 200))
        show_text(screen, "press SPACE to continue", WHITE, 30, (200, 280))
class GameStatus:
    def __init__(self, status, winner=None):
        self.status = status
        self.winner = winner
