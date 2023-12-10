import streamlit as st
from transformers import pipeline

unmasker = pipeline('fill-mask', model='roberta-base')

st.title("Заполнение пропуска")

text = st.text_input("Введите предложение для заполнения пропуска согласно примеру (только на английском языке)", 
	"Hello, i'm <mask> model!")
result = st.button("Заполнить!")
if result:
	variants = unmasker(text)
	st.subheader("Результат подстановки:", divider='rainbow')
	for variant in variants:
		st.write(variant["sequence"])
