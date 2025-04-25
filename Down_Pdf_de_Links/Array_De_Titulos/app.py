import requests
import os

# Lista de links e títulos para baixar
pdf_links = [
    {"title": "Leitura Digital (PDF para download)check", "url": "https://kosmos-cronograma-anexo.s3.amazonaws.com/5594179/3785de08-eaf4-4e01-ac01-055975651f9a.pdf"},
   ]

# Cria a pasta de downloads
pasta = 'downloads'
os.makedirs(pasta, exist_ok=True)

# Baixa os PDFs apenas se o link for um PDF
for item in pdf_links:
    titulo = item["title"]
    url = item["url"]
    
    # Verifica se a URL termina com .pdf
    if url.lower().endswith('.pdf'):
        # Nome do arquivo baseado no título (remover caracteres inválidos para o sistema de arquivos)
        nome_arquivo = ''.join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in titulo) + '.pdf'
        caminho_arquivo = os.path.join(pasta, nome_arquivo)

        try:
            print(f'🔽 Baixando: {titulo} -> {url}')
            response = requests.get(url)
            response.raise_for_status()

            with open(caminho_arquivo, 'wb') as f:
                f.write(response.content)

            print(f'✅ Salvo como: {caminho_arquivo}\n')
        except Exception as e:
            print(f'❌ Erro ao baixar {url}: {e}\n')
    else:
        print(f'⚠️ Ignorado (não é PDF): {url}')
