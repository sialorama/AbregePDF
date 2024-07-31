# Application AbregePDF:  
  
Cette application Streamlit permet de charger un fichier PDF et de générer le résumé de celui ci.    

Installation des dépendances:  
Vous aurez besoin d'installer les bibliothèques nécessaires. 
Utilisez les commandes suivantes pour installer Streamlit, PyMuPDF et transformers :

```
pip install streamlit PyMuPDF transformers
```
Explication du code
Importation des bibliothèques :

fitz pour lire le contenu des fichiers PDF.
pipeline de transformers pour générer des résumés.
Fonction read_pdf :

Cette fonction lit le contenu textuel de toutes les pages d'un fichier PDF et retourne le texte.
Fonction principale main :

Configure la page Streamlit.
Affiche le titre et la description de l'application.
Crée un widget pour télécharger des fichiers PDF.
Lorsque l'utilisateur clique sur le bouton "Résumer", le fichier PDF est lu, et son contenu est résumé en utilisant un modèle de summarization de Hugging Face.
Exécution de l'application :

La fonction main est appelée pour démarrer l'application lorsque le script est exécuté.
Lancement de l'application.

Pour lancer l'application, utilisez la commande suivante dans votre terminal :

```
streamlit run app.py

```
