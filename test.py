import requests
import folium

# Liste des adresses IP que vous souhaitez localiser
ip_addresses = ["158.190.216.241", "95.101.36.64", "95.100.173.65"]

# Créer une carte vide
m = folium.Map(location=[0, 0], zoom_start=2)

# Interroger le service d'IP Geolocation pour chaque adresse IP
for ip in ip_addresses:
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    data = response.json()
    location = data.get("loc").split(",")
    
    # Ajouter un marqueur sur la carte
    folium.Marker(location=[float(location[0]), float(location[1])], tooltip=ip).add_to(m)

# Enregistrez la carte dans un fichier HTML
m.save("carte_routeurs.html")
