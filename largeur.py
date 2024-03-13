def ParcoursLargeur(G):
    # Initialisation
    p = {}
    Atteint = {}
    profondeurs = {}  # Table des profondeurs
    début = 0
    fin = 0
    
    for sommet in G.keys():
        p[sommet] = 0  # Affectation de la valeur 0 à chaque sommet

    while any(p[S0] == 0 for S0 in p.keys()):  # Utilisation de any() pour vérifier s'il existe un sommet non visité
        for S0 in p.keys():
            if p[S0] == 0:
                p[S0] = S0  # Marquer le sommet comme visité
                fin += 1
                Atteint[fin] = S0  # Ajout du sommet à la liste Atteint
                profondeurs[S0] = 0  # Initialisation de la profondeur à 0 pour le sommet racine
        while début < fin:
            début += 1
            S = Atteint[début]
            for t in G[S]:
                if p[t] == 0:
                    fin += 1
                    Atteint[fin] = t
                    p[t] = S
                    profondeurs[t] = profondeurs[S] + 1  # Profondeur de t est la profondeur de S plus 1
    return p, profondeurs  # Retourner à la fois la table des pères et la table des profondeurs

# Exemple de graphe
G = {
    '1': ['2', '4'],
    '2': ['1', '3'],
    '3': ['2', '5'],
    '4': ['1', '5'],
    '5' : ['3', '4'],
    '6' : ['7'],
    '7' : ['6']
}

#  1-----2-----3
#  |           |
#  |           |
#  |           |
#  4-----------5  6-----7

# Appel de la fonction ParcoursLargeur avec le graphe donné
resultat_p, resultat_profondeurs = ParcoursLargeur(G)
print("Table des pères:", resultat_p)
print("Table des profondeurs:", resultat_profondeurs)
