# Python3.7
# -*-coding:UTF-8 -*
# Table de multiplication avec la boucle while
# TP by Yishan le 29/12/2018

import os

nb = input("Saissisez votre table de multiplication : ")
nb = int(nb)

i = 0

while i < 10:
	print(i + 1, "*", nb, "=", (i + 1) * nb)
	i += 1

os.system("pause")