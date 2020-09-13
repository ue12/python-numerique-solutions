import numpy as np

def super_checkers(n, k):
    """
    construit un damier dans un carré de coté n*k
    avec des briques de taille k x k
    alternativement vraies et fausses

    on décide arbitrairement que 
    """
    size = k*n
    # indices() à la rescousse
    I, J = np.indices((size, size))
    # la périodicité c'est 2k
    # l'opérateur ^ fait un XOR bit-à-bit
    return (I % (2*k) < k) ^ (J % (2*k) < k)
