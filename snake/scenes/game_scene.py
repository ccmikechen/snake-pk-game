import pygame
from snake.resource import R
from random import randint
from math import sqrt
from snake.scene import Scene
from snake.ui.player import Player
from snake.ui.food import Food
from snake.ui.game_info import GameInfo
from snake.animations.blood_animation import BloodAnimation
from snake.game_helper import show_text

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
FOOD_COLORS = [YELLOW, GREEN]
GAME_OVER = "game_over"
DRAW = "draw"
CONTINUE = "continue"

MAX_FOODS = 50

class GameScene(Scene):
    def setup(self):
        self.reset()
        self.game_info = GameInfo(self.game.get_bound())

    def reset(self):
        self.is_running = True
        self.game_status = None
        self.player_1 = Player(self, (100, 100), BLUE)
        self.player_1.add_snake_length(10)
        self.player_2 = Player(self, (600, 100), RED)
        self.player_2.add_snake_length(10)
        self.foods = []

    def get_game_status(self):
        player_1_collisions = self.count_collisions(self.player_1)
        player_2_collisions = self.count_collisions(self.player_2)

        if player_1_collisions > 5 or player_2_collisions > 5:
            if player_1_collisions > player_2_collisions:
                return GameStatus(GAME_OVER, winner=self.player_2, loser=self.player_1)
            elif player_1_collisions < player_2_collisions:
                return GameStatus(GAME_OVER, winner=self.player_1, loser=self.player_2)
            else:
                return GameStatus(DRAW, loser=self.player_1)

        return GameStatus(CONTINUE)

    def count_collisions(self, player):
        collision_count = player.check_collision([self.player_1.snake, self.player_2.snake])

        return collision_count

    def generate_food(self):
        (x_bound, y_bound) = self.game.get_bound()
        x = randint(20, x_bound - 20)
        y = randint(20, y_bound - 20)
        size = 20
        color = FOOD_COLORS[randint(0, len(FOOD_COLORS) - 1)]
        self.foods.append(Food((x, y), size, color))

    def check_eating_foods(self, player):
        for food in self.foods:
            if self.check_food_collision(player.snake, food):
                food.active(player.snake)
                self.foods.remove(food)

    def check_food_collision(self, snake, food):
        head = snake.body.get_head()
        distance = sqrt((head[0] - food.position[0])**2 + (head[1] - food.position[1])**2)

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
            self.game_info.update(delta, {
                "score_1": self.player_1.get_score() - 11,
                "score_2": self.player_2.get_score() - 11
            })
            self.game_status = self.get_game_status()

            if self.game_status.status != CONTINUE:
                R.get_sound("dead").play()
                loser_pos = self.game_status.loser.get_position()
                animation_pos = (loser_pos[0] - 50, loser_pos[1] - 40)
                self.play_animation(BloodAnimation(1.0, animation_pos, (100, 100)))
                self.is_running = False
        super().update(delta)

    def render(self, screen):
        screen.fill((0, 0, 0))

        background = pygame.transform.scale(R.get_image("dirt"), self.game.get_bound())
        screen.blit(background, (0, 0))

        for food in self.foods:
            food.render(screen)

        self.player_1.render(screen)
        self.player_2.render(screen)

        if self.game_status != None:
            if self.game_status.status == GAME_OVER:
                self._show_winner_message(screen, self.game_status.winner)
            elif self.game_status.status == DRAW:
                self._show_draw_message(screen)

        self.game_info.render(screen)
        super().render(screen)

    def on_key_down(self, key):
        if key == pygame.K_SPACE:
            if not self.is_running:
                self.reset()
        if key == pygame.K_BACKSPACE:
            self.start_scene("menu")
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
        bound = self.game.get_bound()
        center_pos = (bound[0] / 2, bound[1] / 3)

        if winner == self.player_1:
            show_text(screen, "Player 1 win", BLUE, 50, center_pos, align_hor="center", align_ver="center")
        elif winner == self.player_2:
            show_text(screen, "Player 2 win", RED, 50, center_pos, align_hor="center", align_ver="center")

        show_text(screen, "press SPACE to continue", WHITE, 30, (center_pos[0], center_pos[1] + 100), align_hor="center", align_ver="center")

    def _show_draw_message(self, screen):
        bound = self.game.get_bound()
        center_pos = (bound[0] / 2, bound[1] / 3)

        show_text(screen, "Draw", WHITE, 50, center_pos, align_hor="center", align_ver="center")
        show_text(screen, "press SPACE to continue", WHITE, 30, (center_pos[0], center_pos[1] + 100), align_hor="center", align_ver="center")
class GameStatus:
    def __init__(self, status, winner=None, loser=None):
        self.status = status
        self.winner = winner
        self.loser = loser
