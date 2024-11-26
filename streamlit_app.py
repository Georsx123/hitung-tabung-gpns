import streamlit as st

st.title("Menghitung :blue[Volume Tabung] :rocket:")

r = st.number_input("Masukan jari-jari (cm): ",0)
t = st.number_input("Masukan tinggi (cm): ",0)

if st.button("Hitung volume",type"primary"):
  v = math.pi*(r**2)*t
  st.success(f"Volume tabung adalah {v:.2f}")
