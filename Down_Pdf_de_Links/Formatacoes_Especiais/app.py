import requests
import os
import re

# Função para formatar o nome do arquivo
def formatar_nome(link):
    nome_arquivo = os.path.basename(link)
    nome_sem_extensao = os.path.splitext(nome_arquivo)[0]

    # Substitui underline por espaço temporariamente
    nome_formatado = nome_sem_extensao.replace('_', ' ')

    # Remove partes desnecessárias (como 'm1' se quiser)
    # nome_formatado = re.sub(r'\bm\d+\b', '', nome_formatado)  # remove 'm1', 'm2', etc

    # Coloca letra maiúscula no início de cada palavra
    nome_formatado = nome_formatado.title()

    # Substitui espaços por underline novamente
    nome_formatado = nome_formatado.replace(' ', '_')

    # Ajuste único para separar números das letras com underscore
    nome_formatado = re.sub(r'(\D)(\d)', r'\1_\2', nome_formatado)

    return f"{nome_formatado}.pdf"

# Lista de links dos PDFs
links = [
    '',
]

for link in links:
    nome_formatado = formatar_nome(link)
    print(f'Baixando: {link} → {nome_formatado}')
    
    response = requests.get(link)
    with open(nome_formatado, 'wb') as f:
        f.write(response.content)

print("Download finalizado com nomes formatados!")
