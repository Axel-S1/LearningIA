import csv
import numpy as np
import matplotlib.pyplot as plt


def read_csv_to_numpy(filename):
    # Initialiser une liste pour stocker les données lues depuis le CSV
    data = []
    
    # Ouvrir le fichier CSV et lire les lignes
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Ignorer l'en-tête si présent
        # Ajouter chaque ligne (transformée en float) à la liste `data`
        for row in csv_reader:
            data.append([float(item) for item in row])
    
    # Convertir la liste `data` en une matrice NumPy
    return np.array(data)

def affiche_graphe_de_comparaison(matrix, collum):
    # Créer le graphique
    plt.figure(figsize=(20, 5))
    plt.plot(matrix[:, 0], matrix[:, collum], label="Données de la deuxième colonne", color="g")
    
    # Ajouter un titre et des labels
    plt.title("Graphique de la deuxième colonne")
    plt.xlabel("Timestamp")
    plt.ylabel("Valeurs")
    
    # Ajouter une grille et une légende
    plt.grid(True)
    plt.legend()

    # Afficher le graphique
    plt.show()