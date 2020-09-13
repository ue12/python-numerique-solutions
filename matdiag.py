
##################################################
# matdiag
##################################################
import numpy as np

def matdiag(liste):
    """
    si les arguments sont x1, x2, .. xn
    retourne une matrice carrée n x n 
    dont les éléments valent
    m[i, j] = xi si i == j
    m[i, j] = 0 sinon
    
    """
    # on initialise avec des zéros
    n = len(liste)
    resultat = np.zeros((n, n))
    # la première méthode est naive
    # ce n'est pas la meilleure façon de faire
    # mais c'est simple à écrire et à comprendre
    for i in range(n):
        resultat[i, i] = liste[i]
    return resultat


##################################################
# matdiag_bis
##################################################
def matdiag_bis(liste):
    """
    pareil mais un peu plus subtil
    """
    # on initialise avec des zéros
    n = len(liste)
    resultat = np.zeros((n, n))
    for i, item in enumerate(liste):
        resultat[i, i] = item
    return resultat


##################################################
# matdiag_ter
##################################################
def matdiag_ter(liste):
    """
    même propos mais cette fois avec du slicing
    """
    # 
    # on initialise un tableau de la bonne taille n x n
    # mais tout à plat, avec des zéros
    n = len(liste)
    plat = np.zeros((n * n,))
    #
    # dans cette représentation là la diagonale correspond
    # à un slice qui commence à 1 avec un pas de n+1
    plat[0 : : n+1] = liste
    # 
    # maintenant on peut remettre
    # dans une forme n x n avec reshape
    #
    return plat.reshape((n, n))


##################################################
# matdiag_quater
##################################################
def matdiag_quater(liste):
    """
    bon maintenant qu'on s'est bien creusé les méninges
    pour le faire à la main, il se trouve qu'il y a 
    - bien sûr - une fonction pour ça dans numpy
    """
    return np.diag(liste)

