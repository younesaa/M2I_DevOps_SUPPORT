import matplotlib.pyplot as plt
import csv
import numpy as np

def read_csv(filename):
    """
    Lit un fichier CSV et extrait deux colonnes de données sous forme de listes.
    
    :param filename: Le nom du fichier CSV à lire.
    :return: Deux listes de données flottantes.
    """
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Ignorer l'en-tête
        summer_data = []
        correlated_data = []
        for row in csv_reader:
            summer_data.append(float(row[1]))
            correlated_data.append(float(row[2]))
        return summer_data, correlated_data

def calculate_correlation(x, y):
    """
    Calcule la corrélation entre deux ensembles de données.
    
    :param x: Première liste de données.
    :param y: Deuxième liste de données.
    :return: Valeur de corrélation.
    """
    corr_matrix = np.corrcoef(x, y)
    correlation = corr_matrix[0, 1]
    return correlation

def plot_scatter(x, y):
    """
    Crée un graphique de dispersion à partir de deux ensembles de données.
    
    :param x: Données pour l'axe des abscisses.
    :param y: Données pour l'axe des ordonnées.
    """
    plt.scatter(x, y)
    plt.xlabel('Summer Data')
    plt.ylabel('Highest Correlated Data')
    plt.title('Scatter Plot of Data Correlation')
    plt.grid(True)

# Utilisation des fonctions définies ci-dessus
if __name__ == "__main__":
    summer_data, highest_correlated_data = read_csv('correlate-summer.csv')
    correlation_value = calculate_correlation(summer_data, highest_correlated_data)
    print(f'Highest correlation: {correlation_value}')
    plot_scatter(summer_data, highest_correlated_data)
    plt.show()