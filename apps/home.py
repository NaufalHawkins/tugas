import streamlit as st
from collections import Counter

# Daftar kata ganti personal dalam bahasa Jerman
personal_pronomen = ["ich", "du", "er", "sie", "es", "wir", "ihr", "sie", "Sie"]


# Fungsi untuk memeriksa apakah sebuah kata adalah kata ganti personal
def is_personal_pronomen(word):
    return word.lower() in personal_pronomen


# Fungsi untuk menghitung frekuensi kata ganti personal dalam teks
def count_personal_pronomen(text):
    words = text.split()
    # Filter hanya kata ganti personal
    pronouns = [word.lower() for word in words if is_personal_pronomen(word)]
    # Hitung frekuensi kata ganti
    return Counter(pronouns)


# Aplikasi Streamlit
def app():
    st.title("Personal Pronoun Frequency Analyzer")

    # Slider untuk mengatur tinggi area teks
    height = st.slider("Set the height of the text area", 100, 1000, 250)

    # Input teks
    text = st.text_area("Input your text here:", height=height)

    # Analisis kata ganti personal
    if st.button("Analyze Personal Pronouns"):
        results = count_personal_pronomen(text)
        st.write("### Personal Pronoun Frequency:")
        if results:
            for pronoun, freq in results.items():
                st.write(f"{pronoun}: {freq}")
        else:
            st.write("No personal pronouns found in the text.")
