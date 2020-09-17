
##################################################
# xixj
##################################################
import numpy as np

def xixj(*args):
    """
    si les arguments sont x1, x2, .. xn
    retourne une matrice carrée n x n
    dont les éléments valent
    m[i, j] = xi * xj

    première solution à base de produit usuel
    entre un vecteur et une colonne, en utilisant
    le broadcasting

    credits: JeF29
    """

    # une ligne qui contient x1, .. xn
    line = np.array(args)
    # habile façon de reshaper automatiquement
    column = line.reshape(-1, 1)
    # on aurait pu faire aussi
    #column = line[:, np.newaxis]
    return line * column


##################################################
# xixj_2
##################################################
def xixj_2(*args):
    """
    pareil mais on construit la colonne avec .T
    qui est la transposée - méfiance quand même
    """
    # sauf que pour pouvoir utiliser .T il faut
    # une shape qui est explicitement [1, n]
    #
    # c'est pourquoi moi j'ai tendance à éviter .T
    # voyez plutôt np.transpose() si vous avez besoin
    # de transposer une matrice
    line = np.array(args).reshape((1, -1))
    return line * line.T


##################################################
# xixj_3
##################################################
def xixj_3(*args):
    """
    on peut aussi penser à faire un produit matriciel
    """
    # on doit lui donner une dimension 2 même si c'est une ligne
    line = np.array(args).reshape((1, -1))
    column = line.reshape((-1, 1))
    return column @ line


##################################################
# xixj_4
##################################################
def xixj_4(*args):
    """
    pareil mais en utilisant .dot()
    """
    column = np.array(args).reshape((-1, 1))
    # dans cette version on fait le produit de matrice
    # en utilisant la méthode dot sur les tableaux
    return column.dot(column.T)
    # remarquez qu'on aurait pu faire aussi bien
    # return np.dot(column, column.T)

