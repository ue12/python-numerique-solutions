
##################################################
# power
##################################################
def power(x, n):
    """
    mise à la puissance en O(log2(n))
    """
    # on s'astreint à ne pas utiliser ** parce que ce serait triché
    # mais bien sûr dans la pratique
    # on pourrait utiliser **2 pour traiter le cas où n est pair
    if n == 1:
        return x
    elif n % 2 == 0:
        # on met au carré power(x, n//2)
        # une petite subtilité ici, c'est que si vous écrivez
        # root = power(x, n//2) * power(x, n//2)
        # vous allez évaluez **deux fois** power()
        # et du coup vous perdez tout le bénéfice de l'exercice
        root = power(x, n//2)
        return root * root
    else:
        return x * power(x, n-1)

