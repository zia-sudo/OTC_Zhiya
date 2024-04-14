import os
import re

def clean(text):
    return re.sub(r"Page \d+", "", text)

def clean(text):
    # Supprimer les numéros de page
    text = re.sub(r"Page \d+", "", text)
    return text.strip()  # Retourner le texte nettoyé sans espaces au début et à la fin

def clean_files(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".txt"):
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_folder, "results", file)

                with open(input_file_path, "r", encoding="utf-8") as f:
                    text = f.read()

                clean_content = clean(text)

                # Créer le dossier "results" s'il n'existe pas déjà
                os.makedirs(os.path.join(output_folder, "results"), exist_ok=True)

                with open(output_file_path, "w", encoding="utf-8") as f:
                    f.write(clean_content)

    print("Tous les fichiers ont été nettoyés et enregistrés dans le répertoire : '{}'.".format(os.path.join(output_folder, "results")))

# Dossiers d'entrée et de sortie
input_folder = "./raw/results/"
output_folder = "./clean/"

# Appel de la fonction pour nettoyer les fichiers
clean_files(input_folder, output_folder)