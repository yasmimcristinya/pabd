import streamlit as st

import controller.cliente as cliente

def deletar():
    st.session_state.dele = False
    st.title("deletar dados")

    with st.form(key='delete'):
        delete_id = st.number_input(label='Insira o id:')
        button_delete_select = st.form_submit_button('deletar')

        if button_delete_select:
            cliente.excluir(int(delete_id))
            st.success('cliente deletado com sucess!!')
    
    