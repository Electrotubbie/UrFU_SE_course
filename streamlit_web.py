import streamlit as st
from unmask import unmasker

st.title("Заполнение пропуска")
st.divider()
text = st.text_input("Введите предложение для заполнения пропуска согласно примеру", 
	"Привет, я <mask> модель!")
result = st.button("Заполнить!")
if result:
	variants = unmasker(text)
	st.subheader("Результат подстановки:", divider='rainbow')
	for variant in variants:
		st.write(variant["sequence"])
