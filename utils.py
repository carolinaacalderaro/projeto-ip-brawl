import pygame
import os
import math

def carregar_imagem(caminho, tamanho=None, alpha=True):
    if not os.path.exists(caminho):
        print(f"Aviso: Imagem não encontrada em -> {caminho}")
        return None
        
    img = pygame.image.load(caminho)
    img = img.convert_alpha() if alpha else img.convert()
    
    if tamanho:
        img = pygame.transform.scale(img, tamanho)
        
    return img

def calcular_escala_respiracao(tempo_ou_ticks, amplitude, velocidade=1.0, base=1.0):
    return base + math.sin(tempo_ou_ticks * velocidade) * amplitude

def deve_desenhar_piscando(contador_frames, intervalo_frames):
    return (contador_frames // intervalo_frames) % 2 == 0

def checar_saida(evento):
    if evento.type == pygame.QUIT:
        return True
    if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
        return True
    return False

def desenhar_texto_contornado(tela, texto, fonte, cor_texto, cor_contorno, x, y):
    deslocamentos = [(-2, -2), (0, -2), (2, -2), (-2, 0), (2, 0), (-2, 2), (0, 2), (2, 2)]
    for dx, dy in deslocamentos:
        surf_borda = fonte.render(texto, True, cor_contorno)
        tela.blit(surf_borda, surf_borda.get_rect(center=(x + dx, y + dy)))
    
    surf_texto = fonte.render(texto, True, cor_texto)
    tela.blit(surf_texto, surf_texto.get_rect(center=(x, y)))