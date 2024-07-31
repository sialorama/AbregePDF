import streamlit as st
import fitz  # PyMuPDF
from transformers import pipeline

# Fonction pour lire le texte d'un PDF
def read_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Fonction principale pour exécuter l'application Streamlit
def main():
    # Configuration de la page
    st.set_page_config(page_title="AbrègePDF")

    st.title("Résumez votre fichier PDF")  # Titre de l'application
    st.write("Créer de manière pertinente et en un clic un résumé de votre fichier PDF")  # Description

    # Création d'un widget de téléchargement de fichier
    pdf = st.file_uploader("Chargez votre fichier PDF", type='pdf')
    submit = st.button("Résumer")

    if submit and pdf:
        with st.spinner("Traitement du fichier..."):
            # Lecture du contenu du PDF
            text = read_pdf(pdf)

            # Génération du résumé
            summarizer = pipeline("summarization")
            summary = summarizer(text, max_length=150, min_length=30, do_sample=False)

            st.subheader("Résumé")
            st.write(summary[0]['summary_text'])

# Exécution de l'application
if __name__ == "__main__":
    main()  # Appel de la fonction principale pour démarrer
