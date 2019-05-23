import pygame
from os import path
from init import BLACK, img_dir, WIDTH, HEIGHT


class GolEsquerdo(pygame.sprite.Sprite):
    
    #Construtor da classe
    def __init__(self):
        
        #Construtor da classe pai (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        #Carregando a imagem de fundo
        player_img= pygame.image.load(path.join(img_dir,"Gol2.png")).convert()
        self.image= player_img
        
        #Diminuindo o tamanho da imagem
        self.image= pygame.transform.scale(player_img,(100,400))
        
        #Deixando transparente
        self.image.set_colorkey(BLACK)
        
        #Detalhes sobre o posicionaento
        self.rect= self.image.get_rect()
        
        #Centraliza embaixo da tela
        self.rect.centerx= WIDTH-1175
        self.rect.bottom= HEIGHT-60
        
   
