import pickle
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title='Previsão de Churn de clientes',
    page_icon='img/dnc.webp'
)

st.write('# Predição churn de clientes')
st.write('\n\n')

st.image('img/customer_churn.jpeg')
st.write('\n\n')

st.write(
"""
    Este modelo de aprendizado de máquina tem como objetivo auxiliar uma empresa de telecomunicações
    que está enfrentando desafios com o churn de clientes. Para isso,
    foi desenvolvido um modelo de machine learning que visa proporcionar à empresa uma compreensão mais aprofundada
    dessa situação

    No contexto de um aplicativo de previsão de churn baseado em aprendizado de máquina,
    a previsão de churn refere-se ao processo de identificar os clientes que têm maior probabilidade
    de deixar de usar os produtos ou serviços de uma empresa.
    O aplicativo utiliza dados históricos e algoritmos de aprendizado de máquina para
    analisar os padrões e comportamentos de clientes anteriores que já cancelaram seus serviços, e,
    em seguida, aplica esse conhecimento para identificar os clientes mais propensos a sair no futuro.
    Ao prever com precisão o churn dos clientes,
    uma empresa pode tomar medidas proativas para manter seus clientes valiosos
    e minimizar o impacto negativo do churn em seus resultados financeiros.
"""
)

st.success('Por favor, **vá para as próximas páginas** para realizar a predição')



