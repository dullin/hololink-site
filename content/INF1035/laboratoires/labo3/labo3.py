import math


def inverse_additif(nombre):
    """
    L'inverse additif d'un nombre.
    Trouve la valeur du nombre multiplié par -1.

    Args:
      nombre (float):  Le nombre à inverser.
    Returns:
      float: L'inverse du nombre.

    Exemple:
      ::

          >> inverse_additif(45)
               -45

      ::

          >> inverse_additif(-4.5)
                4.5

    """

    return -nombre


def inverse_multiplicatif(nombre):
    """
    L'inverse multiplicatif.
    Retourne la valeur à la puissance -1.

    Args:
      arg1 (float): La valeur dont on veut retourner l'inverse.
    Returns:
      float: L'inverse multiplicaitf de la valeur de départ.

    Exemple:
      ::

          >> inverse_multiplicatif(5)
                0.2

      ::

          >> inverse_multiplicatif(0.25)
                 4

    """

    return 1/nombre


def compteur_entre_borne(debut, fin):
    """
    La somme en entre un borne minimale et une borne maximale.
    Ex : `debut + (debut+1) + ... + (fin-1) + fin`.
    Args:
      debut (float): La valeur de départ de la sommation à faire.
      fin (float): La valeur de fin de la sommation à faire.
    Returns:
      float: La somme du compteur entre les bornes données.
    Exemple:
      ::

          >> compteur_entre_borne(10, 13)
              46

      ::

          >> compteur_entre_borne(0, 7)
              28

    """

    # Calcule la somme cumulative.
    somme = 0
    for i in range(debut,fin + 1):
        somme = somme + i
    return somme

    # NOTE: Une autre réponse sans l'utilisation de la boucle.
    # La légende dit que que l'équation fut trouvé par Carl Friedrich Gauss
    # durant sont enfance.
    # http://bit-player.org/wp-content/extras/gaussfiles/gauss-snippets.html
    # reponse = (fin - debut + 1) * (debut + fin) / 2;


def factoriel(n):
    """
    Factoriel de n. Retourne la somme multiplicative de 1 à n.

    Args:
      n (float): La valeur pour laquelle on souhaite calculer le factoriel.
    Returns:
      float: La somme multiplicative factoriel du nombre.
      
    Exemple:
      ::

          >> factoriel(5)
               120

    """

    # Trouve la somme cummulative multiplicative de 1 à n.
    fact = 1
    for indice in range(2, n + 1):
        fact = fact * indice
    return fact


def saisit_entre_borne(minimum, maximum):
    """
    Saisi une valeur et recommence tant que la saisit n'est pas à
    l'intérieur de bornes données.
    
    Args:
      minimum (float): La borne inférieure de l'intervalle de saisi.
      maximum (float): La borne supérieure de l'intervalle de saisi.
    Returns:
      float: La valeur finalement saisit entre les bornes.
    
    Exemple:
      ::
    
           >> saisit_entre_borne(5, 10)
             Veuillez entrer une valeur : 3
             La valeur doit se situer entre 5 et 10.
             Veuillez entrer une valeur : 12
             La valeur doit se situer entre 5 et 10.
             Veuillez entrer une valeur : 5
                  5

    """

    # Saisit le premier nombre.
    saisit = float(input('Veuillez entrer une valeur : '))

    # Tant qu'on dépasse une des bornes.
    while (saisit < minimum or saisit > maximum):
        # Recommence la saisie.
        print('La valeur doit se situer entre', minimum, 'et', maximum)
        saisit = float(input('Veuillez entrer une valeur : '))
    return saisit


def maximum_de_deux(nb1, nb2):
    """
    Le nombre maximum entre deux nombres.

    Args:
      nb1 (float): Première valeur a comparer.
      nb2 (float): Seconde valeur a comparer.
    Returns:
      float: La valeur maximum entre les deux nombres.

    Exemple:
      ::

          >> maximum_de_deux(3, 5)
                 5

      ::

          >> maximum_de_deux(34, 34)
                 34

    """

    # Trouve le plus grand nombre.
    if nb1 > nb2:
        return nb1
    else:
        return nb2


def maximum_de_trois(nb1, nb2, nb3):
    """
    Le nombre maximum entre trois nombres.

    Args:
      nb1 (float): Première valeur a comparer.
      nb2 (float): Seconde valeur a comparer.
      nb3 (float): Troisième valeur à comparer.
    Returns:
      float: La valeur maximum entre les trois nombres.

    Exemple:
      ::

          >> maximum_de_trois(3, 5, 2)
                 5

      ::

          >> maximum_de_trois(34, 34, 34)
                 34

      ::

          >> maximum_de_trois(34, 5, 34)
                 34

    """

    # Utilise la fonction précédente pour simplifier le problème.
    return maximum_de_deux(maximum_de_deux(nb1,nb2), nb3)


def maximum_de_quatre(nb1, nb2, nb3, nb4):
    """
    Le nombre maximum entre quatrew nombres.

    Args:
      nb1 (float): Première valeur a comparer.
      nb2 (float): Seconde valeur a comparer.
      nb3 (float): Troisième valeur à comparer.
      nb4 (float): Quatrième valeur à comparer.
    Returns:
      float: La valeur maximum entre les quatre nombres.

    Exemple:
      ::
          >> maximum_de_quatre(3, 5, 2, 1)
                 5

      ::
          >> maximum_de_quatre(34, 34, 34, 34)
                 34

      ::
          >> maximum_de_quatre(34, 5, 34, 45)
                 45

    """

    # Utilise la fonction précédente pour simplifier le problème.
    return maximum_de_deux(maximum_de_deux(nb1, nb2), maximum_de_deux(nb3, nb4))


def pgcd(a, b):
    """
    Le plus grand commun diviseur entre deux nombre. Utilise
    l'algorithme suivant pour y arriver:

      ::

          tant que b diférent de 0
              si a plus grand que b alors
                  a := a - b
              sinon
                  b := b - a
              fin si
          fin tant que
          résultat := a

    Le signe `:=` est une assignation en algorithmie.

    Args:
      a (float): Première valeur.
      b (float): Deuxième valeur.
    Returns:
      float: Plus grand diviseur des deux nombres.

    Exemple:
      ::

          >> pgcd(12, 30)
                 6

      ::

          >> pgcd(8, 4)
                 4

    """

    # Utilise l'algorithme fourni pour trouver les plus grand diviseur.
    while b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


def est_premier(n):
    """
    Détermine si le nombre est premier.
    Retourne `true` si le nombre est premier, `false` autrement.
    
    Args:
      n (float): Le nombre à tester.
    Returns:
      float: `true` si le nombre est premier.
    
    Exemple:
      ::
    
          >> est_premier(4)
            False
    
      ::
          
          >> est_premier(7)
            True

    """

    # Test des cas particuliers.
    if (n == 2):
        premier = True
    elif (n == 1 or n % 2 == 0):
        premier = False
    else:
        # Suppose que le nombre est premier.
        premier = True

        # Vérifie tous les diviseurs impairs entre 2 et sqrt(n).
        # Note : une propriété mathématique nous permet de tester jusqu'à
        # sqrt(n) pour augmenté la rapidité de la fonction.
        racineN = math.sqrt(n)
        indice = 3
        while indice <= racineN and premier == True:
            # Si on trouve un diviseur, alors il n'est pas premier.
            if n % indice == 0:
                premier = False
            #Saut de 2 pour sauter le prochain nombre pair.
            indice = indice + 2

    return premier


def affiche_n_nombre_premier(n):
    """
    Affiche les n nombres premiers dans la fenêtre de commande.

    Args:
      n (float): Le nombre de nombre premiers à afficher.

    Exemple:
      ::

          >> affiche_n_nombre_premier(4)
            1 ieme nombre premier : 2.
            2 ieme nombre premier : 3.
            3 ieme nombre premier : 5.
            4 ieme nombre premier : 7.

    """

    # Compte le nombre généré.
    nAffiche = 0
    i = 1
    while nAffiche < n:
        # Trouve si le prochain indice est premier.
        if est_premier(i):
            # Affiche et garde compte du nombre afficher.
            nAffiche = nAffiche + 1
            print(nAffiche, 'ieme nombre premier : ', i)
        i = i + 1


def n_diviseur(n):
    """
    Le nombre de diviseurs de n.

    Args:
      n (float): Le nombre à tester.
    Returns:
      float: Le nombre de diviseurs du nombre.

    Exemple:
      ::

          >> n_diviseur(45)
                 6

      ::

          >> n_diviseur(8)
                 4

    """

    # Teste tous les diviseurs possibles.
    # Inclus 1 automatique pour augmenter l'efficaciter de la fonction.
    diviseurs = 1
    indice = 2
    while (indice <= n):
        if n % indice == 0:
            diviseurs = diviseurs + 1
        indice = indice + 1
    return diviseurs

    # Note : On pourrait résoudre le problème grâce à la fonction Phi
    # d'Euler qui dit que le nombre de diviseurs d'un nombre
    # est égal au produit des exposants + 1 de sa représentation
    # en nombre premiers.
    # Ex. : 200 = 2^3 * 5^2
    #      Phi(200) == 4 * 3 == 12 == nDiviseurs

