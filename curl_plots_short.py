import subprocess
import matplotlib.pyplot as plt

# URL de destination
url = 'https://www.credit-agricole.fr'  # Remplacez par l'URL de votre choix

# Listes pour stocker les durées des RTT
rtt_durations = []

# Temps total d'exécution en secondes (1 heure = 3600 secondes)
total_execution_time = 3600

# Durée de la requête en secondes (60 secondes = 1 minute)
request_interval = 60

# Boucle pour effectuer les requêtes pendant une heure
import time
start_time = time.time()
while time.time() - start_time < total_execution_time:
    try:
        # Effectuer la requête CURL et mesurer le temps
        curl_command = f'curl -s -w "%{{time_total}}" {url} -o /dev/null'
        result = subprocess.run(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        rtt = float(result.stdout)
        rtt_durations.append(rtt)
        print(f"Durée RTT : {rtt} secondes")
    except Exception as e:
        print(f"Erreur lors de la requête CURL : {e}")
        rtt_durations.append(None)
    
    time.sleep(request_interval)

# Générer l'histogramme
plt.hist(rtt_durations, bins=20, edgecolor='k')
plt.title('Histogramme des durées RTT')
plt.xlabel('Durée RTT (secondes)')
plt.ylabel('Nombre de requêtes')

# Enregistrer l'histogramme dans un fichier PNG
plt.savefig('histogramme_rtt.png')

# Afficher l'histogramme si nécessaire
# plt.show()
