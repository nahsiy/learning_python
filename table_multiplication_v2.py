# python 3.7
# Amélioration de la table de multiplication en créant une fonction
# TP by yishan le 29/12/2018

def table(nb, max):
	"""Fonction affichant la table de multiplication souhaitee"""
	i = 0
	while i < max:
		print(i + 1, "*", nb, "=", (i + 1) * nb)
		i += 1
		
