# -*- coding: utf-8 -*-
"""
Created on Wed May 22 23:39:40 2019

@author: matfs
"""

import pygame
from os import path
from init import BLACK, img_dir, WIDTH, HEIGHT




class Gol_do_player1(pygame.sprite.Sprite):
    
    #Construtor da classe
    def __init__(self):
        
        #Construtor da classe pai (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        #Carregando a imagem de fundo
        Gol_msg_img= pygame.image.load(path.join(img_dir,"GolMsg.png")).convert()
        self.image= Gol_msg_img
        
        #Deixando transparente
        self.image.set_colorkey(BLACK)
        
        #Detalhes sobre o posicionaento
        self.rect= self.image.get_rect()
        
        #Centraliza embaixo da tela
        self.rect.centerx= WIDTH / 2
        self.rect.bottom= HEIGHT - 300