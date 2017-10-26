import sys, pygame

class SpriteSheet(pygame.sprite.Sprite):
    def __init__(self, image_path, frame):
        super().__init__()
        self.sprite_sheet = pygame.image.load(image_path).convert()
        self.frame_width = frame[0]
        self.frame_height = frame[1]

    def image_at(self, x, y):
        image = pygame.Surface([self.frame_width, self.frame_height])
        image.blit(self.sprite_sheet,
                   (0, 0),
                   (x * self.frame_width,
                    y * self.frame_height,
                    self.frame_width,
                    self.frame_height))

        return image
