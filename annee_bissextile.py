# Python3.7
# Ceci est un programme qui permets de déterminer si une année est bissextile ou pas.
# 1er TP by Yishan le 29/12/2018


annee = input("Saisissez une année : ")
annee = int(annee)

if annee % 4 == 0 or annee % 100 == 0 and annee % 400 != 0:
	print("Cette année est bissextile")

else:
	print("Cette année n'est pas bissextile")
