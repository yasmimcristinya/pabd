import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('Inserir Dados')
    
    with st.form(key='insert'):
        input_name = st.text_input(label='Insira o nome da empresa:')
        input_endereco = st.text_input(label='Insira o Endereço:')
        input_telefone = st.number_input(label='Insira o telefone')
    
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(input_name, input_endereco, int(input_telefone))
            st.success('Cliente incluido com sucesso')