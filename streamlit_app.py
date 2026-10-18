import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="streamlit", page_icon="🚀")

st.title("uygulamam")

# 1) İsim selamlama
isim = st.text_input("adın ne?")
if isim:
    st.success(f"merhaba {isim}!")

st.divider()

# 2) Sayaç
if "sayac" not in st.session_state:
    st.session_state.sayac = 0

col1, col2 = st.columns(2)
if col1.button("➕ Arttır"):
    st.session_state.sayac += 1
if col2.button("🔄 Sıfırla"):
    st.session_state.sayac = 0

st.metric("Sayaç", st.session_state.sayac)
