import matplotlib.pyplot as plt
import numpy as np

# Création des données pour la courbe d'équation x²
x = np.linspace(-5, 5, 100)  # Créer un tableau de 100 valeurs entre -5 et 5
y1 = x**2  # Calculer les valeurs de y en utilisant l'équation x²

# Création des données pour la courbe d'équation x³
y2 = x**3  # Calculer les valeurs de y en utilisant l'équation x³

# Tracer les courbes
plt.figure()
plt.plot(x, y1, label='y = x²')  # Tracer la courbe d'équation x²
plt.plot(x, y2, label='y = x³')  # Tracer la courbe d'équation x³
plt.xlabel('x')  # Ajouter une étiquette à l'axe des x
plt.ylabel('y')  # Ajouter une étiquette à l'axe des y
plt.title('Courbes d\'équation x² et x³')  # Ajouter un titre au graphique
plt.legend()  # Ajouter une légende
plt.grid(True)  # Activer la grille
plt.show()  # Afficher le graphique
