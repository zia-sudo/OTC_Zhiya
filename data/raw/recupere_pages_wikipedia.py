import requests
import os
import hashlib
import random

def recuperer_page_aleatoire(langue):
    url = f"https://{langue}.wikipedia.org/api/rest_v1/page/random/summary"
    try:
        reponse = requests.get(url)
        reponse.raise_for_status()  # Vérifie si la requête a échoué
        donnees = reponse.json()
        if 'extract' in donnees and 'title' in donnees:
            return donnees['title'], donnees['extract']
        else:
            print(f"Aucun extrait ou titre trouvé pour une page aléatoire en {langue}")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de la page aléatoire pour {langue}: {e}")
        return None, None

def ecrire_fichier_texte(dossier_data, langue, titre, paragraphe):
    id_unique = generer_id_unique(titre)
    nom_fichier = f"{id_unique}_{langue}.txt"
    chemin_fichier = os.path.join(dossier_data, nom_fichier)
    try:
        with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
            premier_paragraphe = paragraphe.split('\n')[0]  # Extraction du premier paragraphe
            fichier.write(premier_paragraphe.strip() + '\n')  # Écriture du premier paragraphe dans le fichier
    except IOError as e:
        print(f"Erreur lors de l'écriture du fichier {chemin_fichier}: {e}")

def generer_id_unique(titre):
    return hashlib.sha1(titre.encode()).hexdigest()[:8]

def main():
    langues = ['ar', 'en', 'fr', 'es', 'it', 'ja', 'ru', 'th', 'tr', 'vi', 'zh']
    nb_pages_par_langue = 20
    
    # Liste pour stocker les résultats
    resultats = []
    
    for langue in langues:
        dossier_data = f"./raw/results/"
        os.makedirs(dossier_data, exist_ok=True)
        
        for index in range(1, nb_pages_par_langue + 1):
            titre, contenu = recuperer_page_aleatoire(langue)
            
            if titre and contenu:
                # Ajoutez le titre, le contenu et la langue à la liste des résultats
                resultats.append((titre, contenu, langue))
    
    # Mélangez l'ordre des résultats
    random.shuffle(resultats)
    
    # Parcourez les résultats mélangés et écrivez chaque fichier
    for index, (titre, contenu, langue) in enumerate(resultats, start=1):
        print(f"Contenu de l'article {index} ({langue}):")
        print(contenu)
        ecrire_fichier_texte(dossier_data, langue, titre, contenu)
        print(f"Page enregistrée : {titre}_{langue}.txt")

if __name__ == "__main__":
    main()