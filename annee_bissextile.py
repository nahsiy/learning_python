# Python 3.7
# -*-coding:UTF-8 -*
# Ceci est un programme qui permets de déterminer si une année est bissextile ou pas.
# 1er TP by Yishan le 29/12/2018

import os # Module qui dispose de variables et de fonctions utiles pour dialoguer avec votre système d'exploitation

annee = input("Saisissez une année : ")
annee = int(annee)

if annee % 4 == 0 or annee % 100 == 0 and annee % 400 != 0:
	print("Cette année est bissextile")

else:
	print("Cette année n'est pas bissextile")

os.system("pause")