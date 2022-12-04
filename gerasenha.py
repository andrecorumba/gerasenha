import string
from random import choice

import streamlit as st

st.title('Gerasenha')
st.markdown('''Gerador de senhas on line.''')

senha = ''
tamanho = st.slider('Tamanho da Senha', 8, max_value=60)

def gera_senha(tipo, tam):
    senha_gerada = ''
    for i in range(tam):
        senha_gerada +=choice(tipo_valores)
    return senha_gerada

escolha = st.radio('Selecione o tipo de senha',['Somente Letras','Somente Numeros' ,'Letras + Numeros', 'Letras + Numeros + Caracteres Especiais'])

match escolha:
    case 'Somente Letras':
        tipo_valores  = string.ascii_letters
        senha = gera_senha(tipo_valores, tamanho)
    case 'Somente Numeros':
        tipo_valores  = string.digits
        senha = gera_senha(tipo_valores, tamanho)
    case 'Letras + Numeros':
        tipo_valores  =  string.ascii_letters + string.digits
        senha = gera_senha(tipo_valores, tamanho)
    case 'Letras + Numeros + Caracteres Especiais':
        tipo_valores  =  string.ascii_letters + string.digits + string.punctuation
        senha = gera_senha(tipo_valores, tamanho)

st.code(senha)
