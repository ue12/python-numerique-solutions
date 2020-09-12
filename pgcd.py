
##################################################
# pgcd
##################################################
def pgcd(a, b):
    """
    le pgcd de a et b par l'algorithme d'Euclide
    """
    # l'algorithme suppose que a >= b
    # donc si ce n'est pas le cas
    # il faut inverser les deux entrées
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    # boucle sans fin
    while True:
        # on calcule le reste
        reste = a % b
        # si le reste est nul, on a terminé
        if reste == 0:
            return b
        # sinon on passe à l'itération suivante
        a, b = b, reste


##################################################
# pgcd_bis
##################################################
def pgcd_bis(a, b):
    """
    Il se trouve qu'en fait la première
    inversion n'est pas nécessaire.

    En effet si a <= b, la première itération
    de la boucle while va faire:
    reste = a % b  c'est-à-dire a
    et ensuite
    a, b = b, reste = b, a
    provoque l'inversion
    """
    # si l'on des deux est nul on retourne l'autre
    if a * b == 0:
        return a or b
    # sinon on fait une boucle sans fin
    while True:
        # on calcule le reste
        reste = a % b
        # si le reste est nul, on a terminé
        if reste == 0:
            return b
        # sinon on passe à l'itération suivante
        a, b = b, reste


##################################################
# pgcd_ter
##################################################
def pgcd_ter(a, b):
    """
    Une autre alternative, qui fonctionne aussi
    C'est plus court, mais on passe du temps à se
    convaincre que ça fonctionne bien comme demandé
    """
    # si on n'aime pas les boucles sans fin
    # on peut faire aussi comme ceci
    while b:
        a, b = b, a % b
    return a

