#Projeto Dessoft
import pygame
from os import path

from init import BLACK, img_dir, WIDTH, HEIGHT, FPS
from player import Player1

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




#Classe do jogador que representa a nave
class CPU(pygame.sprite.Sprite):
    
    #Construtor da classe
    def __init__(self):
        
        #Construtor da classe pai (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        #Carregando a imagem de fundo
        player_img= pygame.image.load(path.join(img_dir,"SAO.png")).convert()
        self.image= player_img
        
        #Diminuindo o tamanho da imagem
        self.image= pygame.transform.scale(player_img,(50,38))
        
        #Deixando transparente
        self.image.set_colorkey(BLACK)
        
        #Detalhes sobre o posicionaento
        self.rect= self.image.get_rect()
        
        #Centraliza embaixo da tela
        self.rect.centerx= WIDTH/4
        self.rect.bottom= HEIGHT-1200
        
        #Velocidade
        self.speedx=0
    
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

player1=Player1()
player2=CPU()
# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)
        
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
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player1.speedx = -7
                if event.key == pygame.K_RIGHT:
                    player1.speedx = 7
                    
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player1.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player1.speedx = 0
        
        all_sprites.update()
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()




