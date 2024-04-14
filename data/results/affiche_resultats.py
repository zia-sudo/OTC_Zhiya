import os
import csv
import langid

def detect_language(text):
    lang, _ = langid.classify(text)
    return lang

def process_files_in_subdirectories(root_dir, output_dir):
    with open(os.path.join(output_dir, "results.csv"), 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['labels', 'text'])  # Header
        for subdir in os.listdir(root_dir):
            subdir_path = os.path.join(root_dir, subdir)
            if os.path.isdir(subdir_path):
                for file in os.listdir(subdir_path):
                    file_path = os.path.join(subdir_path, file)
                    if file.endswith(".txt"):
                        process_text_file(file_path, csv_writer)

def process_text_file(file_path, csv_writer):
    with open(file_path, 'r', encoding='utf-8') as infile:
        for line in infile:
            text = line.strip()
            if text:  # Vérifie si la ligne n'est pas vide
                lang = detect_language(text)
                csv_writer.writerow([lang, text])

def main():
    clean_dir = "./clean/"  # Chemin vers le répertoire "clean"
    output_dir = "./results/"  # Chemin vers le répertoire de sortie
    os.makedirs(output_dir, exist_ok=True)
    
    process_files_in_subdirectories(clean_dir, output_dir)
    print("Traitement terminé. Les résultats ont été enregistrés dans", os.path.join(output_dir, "results.csv"))

if __name__ == "__main__":
    main()


