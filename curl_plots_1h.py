import subprocess

# URL du site à tester
url = "https://www.credit-agricole.fr"

# Nombre de requêtes à effectuer
num_requests = 50

# Liste pour stocker les temps de réponse
response_times = []

for _ in range(num_requests):
    # Exécute CURL avec les paramètres -s (silencieux) et -w pour formater la sortie
    result = subprocess.run(['curl', '-s', '-w', '%{time_total}\n', url, '-o', '/dev/null'], capture_output=True, text=True)
    
    # Si la requête a réussi, ajoute le temps total à la liste
    if result.returncode == 0:
        response_time = float(result.stdout)
        response_times.append(response_time)

# Calculer la moyenne des temps de réponse
average_response_time = sum(response_times) / num_requests

# Enregistrer les résultats dans un fichier texte
with open("curl_output.txt", "w") as file:
    file.write(f"URL: {url}\n")
    file.write(f"Nombre de requêtes: {num_requests}\n")
    file.write(f"Temps moyen de réponse: {average_response_time:.6f} secondes\n")

# Afficher le résultat à l'écran
print(f"Temps moyen de réponse pour {num_requests} requêtes vers {url}: {average_response_time:.6f} secondes")
