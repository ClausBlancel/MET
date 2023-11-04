import subprocess
from time import sleep
import matplotlib.pyplot as plt

# URL du site à tester
url = "https://www.credit-agricole.fr"

# Nombre de requêtes à effectuer
num_requests = 50

# Liste pour stocker les temps de réponse moyen
average_response_times = []

for _ in range(24) :
    # Liste pour stocker les temps de réponse de chaque requête
    response_times = []
    
    for _ in range(num_requests):
        # Exécute CURL avec les paramètres -s (silencieux) et -w pour formater la sortie
        result = subprocess.run(['curl', '-s', '-w', '%{time_total}\n', url, '-o', '/dev/null'], capture_output=True, text=True)
        
        # Si la requête a réussi, ajoute le temps total à la liste
        if result.returncode == 0:
            response_time = float(result.stdout)
            response_times.append(response_time)

    # Calculer la moyenne des temps de réponse
    average_response_times.append(sum(response_times) / num_requests)
    
    # Attend 1h avant de faire la prochaine opération
    # On peut changer cette valeur pour la remplacer par une plus petite si besoin
    sleep(3600)

# Crée la liste des heures (0-23) pour l'axe des abscisses
hours = list(range(24))

# Crée le plot
plt.figure(figsize=(10, 5))  # Adjust the figure size as needed
plt.plot(hours, average_response_times, marker='o', linestyle='-')
plt.title('Mean Response Time Over the Day')
plt.xlabel('Time')
plt.ylabel('Mean Response Time (seconds)')

# Configure les limites de l'axe des X pour aller de 0 à 23
plt.xlim(0, 23)

#Configure les limites de l'axe des Y pour aller de 0 à 1
plt.ylim(0, 1)

# Affiche la grille
plt.grid(True)

# Enregistre la figure au format png
plt.savefig('response_time_plot.png')