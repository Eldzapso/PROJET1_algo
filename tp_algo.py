# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:48:14 2022

@author: ASUS
"""
from math import *
from abc import ABCMeta, abstractmethod 

class forme_geometrique(metaclass=ABCMeta):
    
    @abstractmethod
    
    def aire(self):
        return  
    def perimetre(self):
        return     
class rectangle(forme_geometrique):
    def __init__(self,hauteur,largeur):# ce sont des attributs
        self.hauteur=hauteur
        self.largeur=largeur
    def aire(self):
        return self.hauteur*self.largeur
    
    def perimetre(self):
        return (self.hauteur+self.largeur)*2
class cercle(forme_geometrique):
    def __init__(self, rayon):
        self.rayon=rayon
    def aire(self):
        return pi*self.rayon**2
    def perimetre(self):
        return 2*pi*self.rayon
        
class triangle(forme_geometrique):
    def __init__(self,AB,BC,AC,hauteur_de_AC):
        self.AB=AB
        self.BC=BC
        self.AC=AC
        self.hauteur_de_AC=hauteur_de_AC
    def aire(self):
        return self.hauteur_de_AC*self.AC/2
    def perimetre (self):
        return self.AB+self.BC+self.AC
class carre(rectangle):
    def __init__(self,cote):
        self.cote=cote
    def aire(self):
        return self.cote*self.cote
    def perimetre(self):
        return self.cote*4
class triangle_rectangle(triangle):
    def __init__(self,AB,AC,hauteur_de_AC):
        self.AB=AB
        self.AC=AC
        self.hauteur_de_AC=hauteur_de_AC
    def aire(self):
        return self.AC*self.hauteur_de_AC/2
    def perimetre (self):
        return self.AB+self.hauteur_de_AC+self.AC
    

    
    