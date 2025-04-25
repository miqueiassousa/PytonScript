import requests
import os

# Função para formatar o nome do arquivo
def formatar_nome(link):
    nome_arquivo = os.path.basename(link)
    nome_formatado = nome_arquivo.replace('_', ' ').title().replace(' ', '_') # title() em Python é um método de string que transforma a primeira letra de cada palavra de uma string em maiúscula
    return f"{nome_formatado}.pdf"

# Lista de links dos PDFs
links = [
    ''  # adicione aqui os links dos PDFs
]

for link in links:
    nome_formatado = formatar_nome(link)
    print(f'Baixando: {link} → {nome_formatado}')
    
    response = requests.get(link)
    with open(nome_formatado, 'wb') as f:
        f.write(response.content)

print("Download finalizado com nomes formatados!")
