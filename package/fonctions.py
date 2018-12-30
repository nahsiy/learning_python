# Python 3.7
# -*-coding:UTF-8 -*
# TP by Yishan le 30/12/2018
# Fonction table


def table(nb, max):
	"""Fonction affichant la table de multiplication souhaitee"""
	i = 0
	while i < max:
		print(i + 1, "*", nb, "=", (i + 1) * nb)
		i += 1