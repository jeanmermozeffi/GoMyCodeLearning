import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Affichage de message
st.title("Hello, Streamlit!")
st.write("Ceci est une application simple avec Streamlit.")

# 4. Utilisation des Widgets (Entrées Interactives)
st.title("Widgets Interactives")
name = st.text_input("Entrez votre nom :")
age = st.slider("Sélectionnez votre age :", 10, 100, 25)

if name:
    st.write(f"Bonjour, {name} ! Vous avez {age} ans.")

# 5. Visualisation de Données
# Créer un DataFrame simple
df = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y': [10, 20, 30, 40, 50]
})

st.dataframe(df)

st.title("Visualisation avec Matplotlib")
st.write("Voici un graphique basé sur un DataFrame Pandas.")

# Tracer le graphique
fig, ax = plt.subplots()
ax.plot(df['X'], df['Y'], marker='o')
st.pyplot(fig)


## 7. Upload de Fichiers

st.title("Upload de Fichiers")

# Chargement du fichier
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Aperçu des données chargées :")
    st.dataframe(data)

# Disposition des Colonnes et Mise en Page

st.title("Disposition des Colonnes")

col1, col2 = st.columns(2)

with col1:
    st.header("Colonne 1")
    st.write("Contenu de la première colonne.")

with col2:
    st.header("Colonne 2")
    st.write("Contenu de la deuxième colonne.")


st.title("Upload de Fichiers")

# Chargement du fichier
uploaded_file1 = st.file_uploader("Choisissez un fichier CSV", type="csv", key=2)

if uploaded_file1 is not None:
    data = pd.read_csv(uploaded_file1)
    st.write("Aperçu des données chargées :")
    st.dataframe(data)

col3, col4, col5 = st.columns(3)

with col3:
    st.header("Colonne 1")
    st.write("Contenu de la première colonne.")

    if st.button("Cliquez-moi"):
        st.write("Vous avez cliqué sur le bouton !")

with col4:
    st.header("Colonne 2")
    st.write("Contenu de la deuxième colonne.")

with col5:
    st.header("Colonne 3")
    st.write("Contenu de la deuxième colonne.")


if st.checkbox("Montrer/masquer ce texte"):
    st.write("Le texte est visible.")

option = st.selectbox("Choisissez une option :", ["Option 1", "Option 2", "Option 3"])
st.write(f"Vous avez sélectionné : {option}")
