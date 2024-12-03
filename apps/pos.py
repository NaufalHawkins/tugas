import streamlit as st
import spacy


def app():
    # Judul aplikasi
    st.title("Part Of Speech (POS) Tagging App")

    # Deskripsi aplikasi
    st.write(
        "Aplikasi ini bertujuan untuk melakukan POS Tagging pada teks yang dimasukkan menggunakan model spaCy."
    )

    # Input teks
    text = st.text_area("Masukkan teks di sini", height=250)

    # Button untuk POS Tagging
    if st.button("Lakukan POS Tagging"):
        try:
            # Muat model spaCy (ganti path jika menggunakan model custom)
            nlp = spacy.load(
                 "./models/de_core_news_sm/de_core_news_sm-3.7.0"
            )  # Pastikan path benar

            # Analisis teks
            doc = nlp(text)

            # Tampilkan hasil POS Tagging dalam format teks yang terstruktur
            st.write("### Hasil POS Tagging:")
            result_text = ""
            for token in doc:
                result_text += f"{token.text} -> {token.pos_}\n"

            st.text(result_text)

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
    else:
        st.write("Masukkan teks untuk memulai POS Tagging.")
