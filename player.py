# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:34:20 2019

@author: matfs
"""
# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'img')

#Classe do jogador que representa a nave
class Player(pygame.sprite.Sprite):
    
    #Construtor da classe
    def __init__(self, nomeimg):
        
        #Construtor da classe pai (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        #Carregando a imagem de fundo
        player_img= pygame.image.load(path.join(img_dir,nomeimg)).convert()
        self.image= player_img
        
        #Diminuindo o tamanho da imagem
        self.image= pygame.transform.scale(player_img(50,38))
        
        #Deixando transparente
        self.image.set_colorkey(BLACK)
        
        #Detalhes sobre o posicionaento
        self.rect= self.image.get_rect()
        
        #Centraliza embaixo da tela
        self.rect.centerx= WIDTH/2
        self.rect.bottom= HEIGHT-10