import streamlit as st
from multiapp import MultiApp
from apps import home, pos, ner

app = MultiApp()

st.sidebar.title("Streamlit Multi-App NLP")

app.add_app("Home", home.app)
app.add_app("POS", pos.app)
app.add_app("NER", ner.app)

app.run()
