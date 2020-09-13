
##################################################
# checkers
##################################################
def checkers(size, corner_0_0=True):
    """
    Un damier
    le coin (0, 0) vaut 1 ou 0 selon corner_0_0
    se souvenir que False == 0 et True == 1
    """
    # on peut voir le damier comme une fonction sur
    # les coordonnées, du genre (i + j) % 2
    # et pour inverser on peut faire un xor
    I, J = np.indices((size, size))
    return (I + J) % 2 ^ corner_0_0


##################################################
# checkers_bis
##################################################
def checkers_bis(size, corner_0_0=True):
    """
    La même chose sur une ligne, avec
    * sum() pour l'addition
    * et logique pour le modulo 2
    * toujours xor pour inverser

    credits: j4l4y
    """
    # avec sum() sur indices()
    # on peut tout faire en une ligne:
    return sum(np.indices((size, size))) & 1 ^ corner_0_0


##################################################
# checkers_ter
##################################################
def checkers_ter(size, corner_0_0=True):
    """
    Une autre approche complètement
    """
    # on part de zéro
    result = np.zeros(shape=(size, size), dtype=int)
    # on remplit les cases à 1 en deux fois
    # avec un slicing astucieux; c'est le ::2 qui fait le travail
    result[1::2, 0::2] = 1
    result[0::2, 1::2] = 1
    # une autre façon de renverser,
    # plutôt que le xor de la première solution
    if corner_0_0:
        result = 1 - result
    return result


##################################################
# checkers_quater
##################################################
def checkers_quater(size, corner_0_0=True):
    """
    Et encore une autre, sans doute pas très lisible
    mais très astucieuse

    credits: j4l4y
    """
    # une utilisation très astucieuse de resize,
    # broadcasting, décalage, bravo !
    return (np.resize((corner_0_0, 1-corner_0_0),
                      (1, size))
            ^ np.arange(size)[:, np.newaxis] & 1)

