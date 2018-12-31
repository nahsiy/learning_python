# Python 3.7
# Exceptions / erreurs
# TP by yishan le 31/12/2018

try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été definie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")
