import pygame

class Scene:
    def __init__(self, game):
        self.game = game

    def update(self):
        raise NotImplementedError()

    def render(self, _screen):
        raise NotImplementedError()

    def start_scene(self, name):
        self.game.start_scene(name)

    def on_key_down(self, _key):
        pass

    def on_key_up(self, _key):
        pass

class ScenesManager:
    def __init__(self, game):
        self.scenes = {}
        self.game = game

    def register(self, scene_class, name):
        scene = scene_class(self.game)
        self.scenes[name] = scene

    def get_scene_by_name(self, name):
        try:
            return self.scenes[name]
        except:
            print("Scene " + name + " is not found")

