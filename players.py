import pygame

# =====================================================================
# CLASSE PLAYER (Jogador Quadrado)
# =====================================================================
class Player:
    def __init__(self, x, y, size=20, color=(0, 128, 255)):
        self.size = size
        self.color = color
        
        # Cria o rect que gerencia a posição e colisão do quadrado
        self.rect = pygame.Rect(x, y, self.size, self.size)
        
        # Velocidade de movimento
        self.speed = 1

    def move(self):
        """Captura as teclas pressionadas e move o quadrado"""
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

    def draw(self, surface):
        """Desenha o quadrado na tela"""
        pygame.draw.rect(surface, self.color, self.rect)


class Player1(Player):
    def __init__(self, x, y, size, color=(255, 255, 255)):
        super().__init__(x, y, size, color)

    def move(self):
        """Captura as teclas pressionadas e move o quadrado"""
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        

class Player2(Player):
    def __init__(self, x, y, size, color=(0, 128, 255)):
        super().__init__(x, y, size, color)

    def move(self):
        """Captura as teclas pressionadas e move o quadrado"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed


