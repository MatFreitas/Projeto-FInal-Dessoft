#Projeto Dessoft
import pygame
from os import path

from init import BLACK, RED, img_dir, snd_dir, fnt_dir, WIDTH, HEIGHT, FPS
from player import Player1
from cpu import CPU
from bola import Bola
from Gol_esquerda import GolEsquerdo
from Gol_Direita import GolDireito
from Gol_do_Player2 import Gol_do_player2
from Gol_do_Player1 import Gol_do_player1

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()


# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("FutCabeça")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

#Carrega o som do jogo
pygame.mixer.music.load(path.join(snd_dir, 'Large-crowd-cheering-and-clapping-sound-effect.mp3'))
pygame.mixer.music.set_volume(0.4)

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'cenario.png')).convert()
background_rect = background.get_rect()
tela_inicio = pygame.image.load(path.join(img_dir, 'telainicio.png')).convert()
IMAGE = pygame.transform.scale(tela_inicio,(WIDTH, HEIGHT))
IMAGE_background = IMAGE.get_rect()  
player1=Player1()
player2=CPU()
bolafut=Bola()
GolE= GolEsquerdo()
GolD= GolDireito()

# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(bolafut)   
all_sprites.add(GolE)
all_sprites.add(GolD)

#Define a variável e a fonte do score
score1 = 0
score2 = 0
score_font = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)

#Define contagem do tempo
countdown = FPS * 30
time = 0

    
# Loop principal.
pygame.mixer.music.play(loops=-1)
running = True
while running:
        
    # Ajusta a velocidade do jogo.
    clock.tick(FPS)
    
    for event in pygame.event.get():
        
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
        
    # A cad a loop, redesenha o fundo e os sprites
    screen.fill(BLACK)
    screen.blit(IMAGE, IMAGE_background)
     
    # Depois de desenhar tudo, inverte o display.
    pygame.display.flip()

# Comando para evitar travamentos.
try:
    
    cont_gol1 = 0
    cont_gol2 = 0
    
    # Loop principal.
    pygame.mixer.music.play(loops=-1)
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
                    if not player1.pulando:
                        player1.speedy = -20
                        player1.pulando = True
                        
                if event.key == pygame.K_LEFT:
                    player2.speedx = -9
                if event.key == pygame.K_RIGHT:
                    player2.speedx = 9
                if event.key == pygame.K_UP:
                    if not player2.pulando:
                        player2.speedy = -20
                        player2.pulando = True
                    
                    
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
        
        #Verifica se houve colisão
        hits = pygame.sprite.collide_rect(player1, player2)
        hits1 = pygame.sprite.collide_rect(player1, bolafut)
        hits2 = pygame.sprite.collide_rect(player2, bolafut)
        
        #Colisão entre players, player1 e bola, player2 e bola, respectivamente
        if hits:
            player1.speedx = -10
            player2.speedx = 10
        if hits1:
            bolafut.speedx = 15
            bolafut.speedy = -15
        if hits2:
            bolafut.speedx = -15
            bolafut.speedy = -15
        
        #Registra gol do player2
        if bolafut.rect.x == 0:
            Gol_P2 = Gol_do_player2()
            all_sprites.add(Gol_P2)
            bolafut.rect.x = WIDTH - 600
            bolafut.rect.y = HEIGHT -400
            player2.rect.x = WIDTH-200
            player2.rect.y = HEIGHT -66
            player1.rect.x = WIDTH-1000
            player1.rect.y = HEIGHT -60
            bolafut.speedx = 0
            bolafut.speedy = -25
            score1 += 1
            cont_gol2 += 1
            
        #Registra gol do player1   
        if  1150 < bolafut.rect.x < WIDTH:
            Gol_P1 = Gol_do_player1()
            all_sprites.add(Gol_P1)
            bolafut.rect.x = WIDTH - 600
            bolafut.rect.y = HEIGHT -400
            player2.rect.x = WIDTH-200
            player2.rect.y = HEIGHT -66
            player1.rect.x = WIDTH-1000
            player1.rect.y = HEIGHT -60
            bolafut.speedx = 0
            bolafut.speedy = -25
            score2 += 1
            cont_gol1 += 1
            
        if cont_gol1 > 0:
            cont_gol1 += 1
            if cont_gol1 == FPS * 0.75:
                Gol_P1.kill()
                cont_gol1 = 0
                
        if cont_gol2 > 0:
            cont_gol2 += 1
            if cont_gol2 == FPS * 0.75:
                Gol_P2.kill()
                cont_gol2 = 0
                
        countdown -= 1
        
        
            
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Desenha o score
        text_surface = score_font.render("{:02d} x {:02d}".format(score2, score1), True, RED)
        countdown_surface = score_font.render("{:02d}".format(countdown), True, RED)
        countdown_rect = countdown_surface.get_rect()
        countdown_rect.midtop = (WIDTH / 2, 40)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        screen.blit(text_surface, text_rect)
        screen.blit(countdown_surface, countdown_rect)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()



