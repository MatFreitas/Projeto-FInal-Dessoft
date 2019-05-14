#Projeto Dessoft
import pygame
from os import path

from init import BLACK, img_dir, WIDTH, HEIGHT, FPS
from player import Player1
from cpu import CPU
from bola import Bola
# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()


# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("FutCabeça")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'cenario.png')).convert()
background_rect = background.get_rect()            
player1=Player1()
player2=CPU()
bolafut=Bola()

# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(bolafut)       
 
# Comando para evitar travamentos.
try:
    
    # Loop principal.
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
            
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                
                        
                if event.key == pygame.K_a:
                    player1.speedx = -9
                if event.key == pygame.K_d:
                    player1.speedx = 9
                if event.key == pygame.K_w:
                    player1.speedy = -21
                        
                if event.key == pygame.K_LEFT:
                    player2.speedx = -9
                if event.key == pygame.K_RIGHT:
                    player2.speedx = 9
                if event.key == pygame.K_UP:
                    player2.speedy = -20
                    
                    while player2.speedy < 0:
                        
                        clock.tick(FPS)
                        all_sprites.update()
    
                        # A cada loop, redesenha o fundo e os sprites
                        screen.fill(BLACK)
                        screen.blit(background, background_rect)
                        all_sprites.draw(screen)
                        
                        # Depois de desenhar tudo, inverte o display.
                        pygame.display.flip()
                        player2.speedy += 1
                        
                    while player2.speedy < 20:
                        
                        clock.tick(FPS)
                        all_sprites.update()
    
                        # A cada loop, redesenha o fundo e os sprites
                        screen.fill(BLACK)
                        screen.blit(background, background_rect)
                        all_sprites.draw(screen)
                        
                        # Depois de desenhar tudo, inverte o display.
                        pygame.display.flip()
                        player2.speedy += 1
                        
                    
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_a:
                    player1.speedx = 0
                if event.key == pygame.K_d:
                    player1.speedx = 0
                if event.key == pygame.K_w:
                    player1.speedy = 0
                if event.key == pygame.K_LEFT:
                    player2.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player2.speedx = 0
                if event.key == pygame.K_UP:
                    player2.speedy = 0
                    
                
                    
                
        
        all_sprites.update()
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()




