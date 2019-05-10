#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:53:44 2019

@author: thiagodavid
"""
import pygame
from os import path
from init import BLACK, img_dir, WIDTH, HEIGHT


#Classe do jogador que representa a nave
#<<<<<<< HEAD
#class Player1(pygame.sprite.Sprite):
#    
#    #Construtor da classe
#    def __init__(self):
#        
#        #Construtor da classe pai (Sprite)
#        pygame.sprite.Sprite.__init__(self)
#        
#        #Carregando a imagem de fundo
#        player_img= pygame.image.load(path.join(img_dir,"CAM.png")).convert()
#        self.image= player_img
#        
#        #Diminuindo o tamanho da imagem
#        self.image= pygame.transform.scale(player_img(50,38))
#        
#        #Deixando transparente
#        self.image.set_colorkey(BLACK)
#        
#        #Detalhes sobre o posicionaento
#        self.rect= self.image.get_rect()
#        
#        #Centraliza embaixo da tela
#        self.rect.centerx= WIDTH*(3/4)
#        self.rect.bottom= HEIGHT-1200
#        
#        #Velocidade
#        self.speedx=0
#        
#    # Metodo que atualiza a posição da navinha
#    def update(self):
#        self.rect.x += self.speedx
#        
#        # Mantem dentro da tela
#        if self.rect.right > WIDTH:
#            self.rect.right = WIDTH
#        if self.rect.left < 0:
#            self.rect.left = 0
#=======
#
#>>>>>>> 4004a6a8f9254157d967d2d1876a2cee7595d22e

class Player1(pygame.sprite.Sprite):
    
    #Construtor da classe
    def __init__(self):
        
        #Construtor da classe pai (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        #Carregando a imagem de fundo
        player_img= pygame.image.load(path.join(img_dir,"CAM.png")).convert()
        self.image= player_img
        
        #Diminuindo o tamanho da imagem
        self.image= pygame.transform.scale(player_img(50,38))
        
        #Deixando transparente
        self.image.set_colorkey(BLACK)
        
        #Detalhes sobre o posicionaento
        self.rect= self.image.get_rect()
        
        #Centraliza embaixo da tela
        self.rect.centerx= WIDTH*(3/4)
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