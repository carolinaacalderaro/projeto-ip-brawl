import pygame


class Player:
    def __init__(self, x, y, color, controls):
        self.rect = pygame.Rect(x, y, 24, 24)
        self.speed = 1
        self.color = color
        self.controls = controls
        self.hidden = False

    def move(self, mapa):
        old_x = self.rect.x
        old_y = self.rect.y

        keys = pygame.key.get_pressed()

        # movimento direto 
        if keys[self.controls["left"]]:
            self.rect.x -= self.speed
        if keys[self.controls["right"]]:
            self.rect.x += self.speed
        if keys[self.controls["up"]]:
            self.rect.y -= self.speed
        if keys[self.controls["down"]]:
            self.rect.y += self.speed

        # colisão com parede
        for wall in mapa.walls:
            if self.rect.colliderect(wall):
                self.rect.x = old_x
                self.rect.y = old_y

        # colisão com água
        for water in mapa.waters:
            if self.rect.colliderect(water):
                self.rect.x = old_x
                self.rect.y = old_y

        # arbusto (esconder)
        self.hidden = False
        for bush in mapa.bushes:
            if self.rect.colliderect(bush):
                self.hidden = True

    def draw(self, surface):
        if not self.hidden:
            pygame.draw.rect(surface, self.color, self.rect)


class Player1(Player):
    def __init__(self, x, y):     # cor              # controles
        super().__init__(x, y, (0, 0, 255), {"left": pygame.K_a, "right": pygame.K_d, "up": pygame.K_w, "down": pygame.K_s})

class Player2(Player):
    def __init__(self, x, y):     # cor              # controles
        super().__init__(x, y, (255, 0, 0), { "left": pygame.K_LEFT, "right": pygame.K_RIGHT, "up": pygame.K_UP, "down": pygame.K_DOWN})