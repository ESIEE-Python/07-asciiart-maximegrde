"""programme qui permet de réduire des chaînes sous forme tuples (lettre,occ)"""
#### Imports et définition des variables globales
import sys

#### Fonctions secondaires
sys.setrecursionlimit(150000)
def artcode_i(s):
    """fait ce que est dit plus haut de manière itérative"""
    if not s:
        return []  # Si la chaîne est vide, retourner une liste vide
    result = []  # Liste pour stocker les tuples (caractère, nombre d'occurrences)
    count = 1  # Compteur pour les occurrences d'un caractère
    # Parcourir la chaîne à partir du deuxième caractère
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1  # Incrémenter le compteur si le caractère est identique au précédent
        else:
            result.append((s[i-1], count))  # Ajouter le tuple (caractère précédent, nombre d'occ
            count = 1  # Réinitialiser le compteur pour le nouveau caractère
    # Ajouter le dernier caractère et son compteur
    result.append((s[-1], count))
    return result



def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en 
    argument 
    selon un algorithme 
    récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # Cas de base : si la chaîne est vide, retourner une liste vide
    if not s:
        return []
    # Compter les occurrences consécutives du premier caractère
    count = 1
    while count < len(s) and s[count] == s[0]:
        count += 1
# Retourner un tuple (premier caractère, nombre d'occurrences) et appeler récursivement
    return [(s[0], count)] + artcode_r(s[count:])




#### Fonction principale


def main():
    """execute les deux types de manières pour faire le programme"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
