import streamlit as st
import os 

# Main function to run streamlit app
def main():
    # Set page config
    st.set_page_config(page_title="AbrègePDF")

    st.title("Résumez votre fichier PDF") # App title
    st.write("Créer de manière pertinente et en un clic un résumé de votre fichier PDF") # Description

    # Creating a streamlit file uploader widget
    pdf = st.file.uploader("Chargez votre fichier PDF", type='pdf')
    submit = st.button("Résumer")



# App execution
if __name__ == "__main__":
    main() # Calling the main function to start