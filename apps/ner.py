import streamlit as st
import spacy
from spacy import displacy


def app():
    # Judul aplikasi
    st.title("Named Entity Recognition (NER) App")

    # Deskripsi aplikasi
    st.write(
        "Aplikasi ini bertujuan untuk melakukan Named Entity Recognition (NER) pada teks yang dimasukkan menggunakan model spaCy."
    )

    # Input teks
    text = st.text_area("Masukkan teks di sini", height=250)

    # Button untuk NER
    if st.button("Lakukan Named Entity Recognition"):
        try:
            # Muat model spaCy (ganti path jika menggunakan model custom)
            nlp = spacy.load(
                "./models/de_core_news_sm/de_core_news_sm-3.7.0"
            )  # Pastikan path benar

            # Analisis teks
            doc = nlp(text)

            # Menampilkan hasil NER menggunakan Displacy
            st.write("### Hasil Named Entity Recognition (NER):")

            # Menggunakan st.components.v1.html untuk menampilkan output HTML dari displacy.render
            html = displacy.render(
                doc, style="ent", jupyter=False, options={"distance": 100}
            )
            st.components.v1.html(
                html, height=10000
            )  # Menyesuaikan tinggi tampilan sesuai kebutuhan

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
    else:
        st.write("Masukkan teks untuk memulai Named Entity Recognition.")
