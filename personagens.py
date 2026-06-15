import pygame
import os
from players import Player

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CONTROLS_P1 = {"left": pygame.K_a, "right": pygame.K_d, "up": pygame.K_w, "down": pygame.K_s}
CONTROLS_P2 = {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "up": pygame.K_UP, "down": pygame.K_DOWN}

class base_personagens(Player):
     
    standing_file = None
    asset_pasta = None

    def __init__(self, x, y, controls):
         
        def carregar_frame(nome_arquivo, prop1=30, prop2=60):
            caminho = os.path.join(BASE_DIR, "assets", self.asset_pasta, nome_arquivo)
            img = pygame.image.load(caminho).convert_alpha()
            return pygame.transform.scale(img, (prop1, prop2))
                
        self.walkleft = [carregar_frame('L1.png'), carregar_frame('L2.png')]
        self.walkright = [carregar_frame('R1.png'), carregar_frame('R2.png')]
        self.walkup = [carregar_frame('U1.png'), carregar_frame('U2.png')]
        self.walkdown = [carregar_frame('B1.png'), carregar_frame('B2.png')]
        self.standing = carregar_frame('shelly.png', 65, 60)

        super().__init__(x, y, controls)

class shelly(base_personagens):  # Adicionar idealmente os sprites dps de cada personagem
    asset_pasta = "shelly"
    standing_file = "shelly.png"

class piper(base_personagens):
    asset_pasta = "piper"
    standing_file = "piper.png"

class ElPrimo(base_personagens):
    asset_pasta = "elprimo"
    standing_file = "elprimo.png"

class Colt(base_personagens):
    asset_pasta = "colt"
    standing_file = "colt.png"

class Butcher(base_personagens):
    asset_pasta = "butcher"
    standing_file = "butcher.png"

       
