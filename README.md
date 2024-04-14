# OTC_Zhiya
## Première séance

**Tâche que je veux réaliser** :
Token classification (classification de tokens)

**Corpus qui répond à cette tâche** :
Nom:papluca/language-identification
Lien: https://huggingface.co/datasets/papluca/language-identification

**Types de prédiction** :
identifier la langue d'un texte donné

**Langues concernées** :
20 langues au total: l'arabe, le bulgare, l'allemand, le grec moderne, l'anglais, l'espagnol, le français, l'hindi, l'italien, le japonais, le néerlandais, le polonais, le portugais, le russe, le swahili, le thaï, le turc, l'urdu, le vietnamien et le chinois.

**Echantillons** :
 L'ensemble d'entraînement contient 70 000 échantillons, tandis que les ensembles de validation et de test en contiennent chacun 10 000. 

**Modèles utilisés** :
* papluca/xlm-roberta-base-language-detection (précision de 99,6% sur l'ensemble de tests)
* sileod/deberta-v3-base-tasksource-nli
* sileod/deberta-v3-large-tasksource-nli
* sileod/mdeberta-v3-base-tasksource-nli
* dominguesm/xlm-roberta-base-lora-language-detection
* qgyd2021/language_identification

**Informations sur le corpus**:
Source: Collecte de données à partir de trois sources principales : Multilingual Amazon Reviews Corpus, XNLI et STSb Multi MT.
Taille: 90 000 lignes (15,3 Mo)
Composition: Le corpus est composé de passages de texte et de leur étiquette de langue correspondante. Exemple: {'labels': 'fr', 'text': 'Conforme à la description, produit pratique.'}
