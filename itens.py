import pygame

class Itens:
    def __init__(self, x, y, radius=5, color=(255, 0, 0)):
        self.posicao = (x, y)
        self.radius = radius
        self.color = color
        
    def draw(self, surface):
        """Desenha o circulo na tela"""
        pygame.draw.circle(surface, center=self.posicao, radius = self.radius, color=self.color)
        