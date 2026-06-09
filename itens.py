import pygame

class Item:
    def __init__(self, x, y, item_type):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.type = item_type  # "life", "damage", "speed"

        if item_type == "life":
            self.color = (0, 255, 0)
        elif item_type == "damage":
            self.color = (255, 0, 0)
        elif item_type == "speed":
            self.color = (0, 0, 255)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)