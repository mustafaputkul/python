import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="-", page_icon="🚀")

st.title("Uygulama")

isim = st.text_input("adın ne?")
if isim:
    st.success(f"merhaba {isim}!")

st.divider()

if "sayac" not in st.session_state:
    st.session_state.sayac = 0

col1, col2, col3 = st.columns(3)
if col1.button("➕ Arttır"):
    st.session_state.sayac += 1
if col2.button("➖ Azalt"):
    st.session_state.sayac = max(0, st.session_state.sayac - 1)
if col3.button("🔄 Sıfırla"):
    st.session_state.sayac = 0

    
st.metric("Sayaç", st.session_state.sayac)
