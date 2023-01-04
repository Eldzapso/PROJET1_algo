# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 15:39:38 2023

@author: Gloire MBONGA
"""

import math
class rectangle:
    def __init__(self,longueur,largeur):
        self.longueur=longueur
        self.largeur=largeur
    def aire(self):
        return self.longueur*self.largeur
    def perimetre (self):
        return (self.longueur+self.largeur)*2
    
class cercle:
    def __init__(self,rayon):
        self.rayon=rayon
    def aire(self):
        return self.math.pi*self.rayon**2
    def perimetre (self):
        return 2*math.pi*self.rayon