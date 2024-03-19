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

data = st.file_uploader('Upload CSV File')
if data:
    df_input = pd.read_csv(data)
    df_output = df_input.assign(
        churn= model.predict(df_input),
        churn_probability= model.predict_proba(df_input)[:,1]
    )
    
    
    st.markdown('Previsão do Churn')
    st.write(df_output)
    st.download_button(
        label='Download CSV', data=df_output.to_csv(index=False).encode('utf-8'),
        mime='text/csv', file_name='churn_prediction.csv'
        )

 



