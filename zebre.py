import numpy as np

def zebre(n):
    """
    dans le tableau que l'on crée, on trouve
    la parité de l'indice de colonne
    """
    I, J = np.indices((n, n))
    return J % 2
