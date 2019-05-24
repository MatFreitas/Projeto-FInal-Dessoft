#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:54:57 2019

@author: thiagodavid
"""

from os import path

WIDTH=1200
HEIGHT=800

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS=60


# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'img')

#Estabelece a pasta que contem os sons
snd_dir = path.join(path.dirname(__file__), 'snd')

#Estabelece a pasta que contem a fonte
fnt_dir = path.join(path.dirname(__file__), 'fnt')