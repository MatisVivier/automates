def parcours_profondeur(Graphe):
    # Initialisation
    predecesseurs = {}  
    profondeurs = {} 

    # Parcours de tous les sommets dans le graphe
    for sommet in Graphe:
        predecesseurs[sommet] = 0  
        profondeurs[sommet] = 0 

    # Parcours en profondeur pour chaque sommet non visité
    for sommet in Graphe:
        if predecesseurs[sommet] == 0:
            predecesseurs[sommet] = sommet  # Marquer le sommet comme visité
            parcours_profondeur_recursive(sommet, Graphe, predecesseurs, profondeurs, 0)  # Appel de la fonction récursive avec une profondeur initiale de 0

    return predecesseurs, profondeurs

# Fonction récursive pour le parcours en profondeur
def parcours_profondeur_recursive(sommet, Graphe, predecesseurs, profondeurs, profondeur_actuelle):
    # Mise à jour de la profondeur du sommet
    profondeurs[sommet] = profondeur_actuelle

    # Parcours de tous les voisins du sommet
    for voisin in Graphe[sommet]:
        if predecesseurs[voisin] == 0:
            predecesseurs[voisin] = sommet  # Marquer le voisin comme visité
            parcours_profondeur_recursive(voisin, Graphe, predecesseurs, profondeurs, profondeur_actuelle + 1)  # Appel récursif pour le voisin avec une profondeur augmentée de 1

# Exemple de graphe
Graphe = {
    '1': ['2', '4'],
    '2': ['1', '3'],
    '3': ['2', '5'],
    '4': ['1', '5'],
    '5': ['3', '4'],
    '6': ['7'],
    '7': ['6']
}

#  1-----2-----3
#  |           |
#  |           |
#  |           |
#  4-----------5  6-----7


# Appel de la fonction parcours_profondeur avec le graphe donné
resultat_parcours, resultat_profondeurs = parcours_profondeur(Graphe)

# Affichage du résultat
print("Table des prédécesseurs:", resultat_parcours)
print("Table des profondeurs:", resultat_profondeurs)
