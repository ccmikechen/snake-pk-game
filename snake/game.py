import sys, pygame
from snake.resource import R
from snake.scene import ScenesManager

class Game:
    def __init__(self, title, window_size, fps):
        print("Initial game")

        pygame.init()
        pygame.display.set_caption(title)

        self.fps = fps
        self.clock = pygame.time.Clock()
        self.is_running = False

        self.size = window_size
        self.width = window_size[0]
        self.height = window_size[1]
        self.screen = pygame.display.set_mode(self.size, 0, 32)

        self._load_resources()
        self.scenes_manager = ScenesManager(self)

    def start(self):
        if self.is_running:
            print("Game is started")
        else:
            print("Game start")
            self.is_running = True
            self._game_loop()

    def register_scene(self, scene_class, name):
        self.scenes_manager.register(scene_class, name)

    def start_scene(self, name, params={}):
        self.current_scene = self.scenes_manager.get_scene_by_name(name)

    def _load_resources(self):
        R.load()

    def _game_loop(self):
        while self.is_running:
            self._do_events()
            self.render()
            self.update()

    def _do_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.on_close_window()
            elif event.type == pygame.KEYDOWN:
                self.current_scene.on_key_down(event.key)
            elif event.type == pygame.KEYUP:
                self.current_scene.on_key_up(event.key)

    def update(self):
        self.current_scene.update()

    def render(self):
        self.current_scene.render(self.screen)
        pygame.display.update()
        self.clock.tick(self.fps)

    def on_close_window(self):
        pygame.quit()


