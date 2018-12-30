# Python 3.7
# -*-coding:UTF-8 -*
# Création de notre premier module pour le projet table_multiplication
# 1er TP by Yishan le 30/12/2018

""" module multiplication contenant la fonction table """

def table(nb, max=10):
	i = 0
	while i < max:
		print(i + 1, "*", nb, "=", (i + 1) * nb)
		i += 1
