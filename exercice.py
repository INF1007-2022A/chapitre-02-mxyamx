#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    return mot
#Acquisition des donnees
ma_chaine =input('Veuillez entrez une chaine de caractere:')
#2 boucle sur les caracteres
ma_nouvelle_chaine = ''
for caractere in ma_chaine:
    ma_nouvelle_chaine += chr(ord(caractere)-32)
#sortie des donnes
print(ma_nouvelle_chaine)



