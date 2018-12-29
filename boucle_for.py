#python 3.7
# Utiliser la boucle for et in dans une chaine de caractère
# TP by yishan le 29/12/2018


chaine = "J'apprends le python"
for lettre in chaine:
	if lettre in "AEIOUYaeiouy":
		print(lettre)
	
	else:
		print("*")



