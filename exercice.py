#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    ma_nouvelle_chaine = ''
    for caractere in mot :
        ma_nouvelle_chaine += chr(ord(caractere)-32)
    return ma_nouvelle_chaine

if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre',
        'yolo'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)


