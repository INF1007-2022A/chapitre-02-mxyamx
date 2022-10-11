#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    return mot
ma_chaine = input(' Veuillez entrez un mot : ')
ma_nouvelle_chaine = ''
for caractere in ma_chaine:
    ma_nouvelle_chaine += chr(ord(caractere)-32)
print(ma_nouvelle_chaine)




