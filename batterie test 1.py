# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 16:14:28 2022

@author: Gloire MBONGA AND JOSEPH DZAPILI
"""
#orienter objet = heritage
from tp_algo import *
fre=triangle(5,5,6,4)
print("la surface vaut :", fre.aire())
print("le perimetre vaut :", fre.perimetre())
RECT=rectangle(28,60)
print("la surface vaut : ", RECT.aire())
print("le perimetre vaut :", RECT.perimetre())
CAR=carre(25)
print("la surface du carre vaut :", CAR.aire())
print("le perimetre du carre vaut :",CAR.perimetre())
CIRCLE=cercle(48)
print("la surface du cercle vaut {:.2f}".format(CIRCLE.aire()))
print("le perimetre du cercle vaut {:.2f}:".format(CIRCLE.perimetre()))
