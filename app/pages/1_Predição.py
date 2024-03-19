import pickle
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title='Previsão de Churn de clientes',
    page_icon='img/dnc.webp'
)

st.title('Previsão de Churn')

st.markdown("Por favor colocar o arquivo csv para a predição")

#--model--#
with open('models/model.pkl','rb') as model_file:
    model =  pickle.load(model_file)

data = st.file_uploader()

 



