import pygame

class Resource:
    def __init__(self):
        self.images = {}
        self.sounds = {}

    def load(self):
        print("Loading resources...")
        print("Resources loaded.")

    def get_image(self, name):
        try:
            return self.images[name]
        except:
            print("Image " + name + " not found")

    def get_sound(self, name):
        try:
            return self.sounds[name]
        except:
            print("Sound " + name + " not found")

R = Resource()
