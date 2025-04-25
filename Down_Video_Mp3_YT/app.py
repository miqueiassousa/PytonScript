import yt_dlp
import os

# Caminho fixo da pasta onde os arquivos serão salvos
pasta_destino = "musicas"

# Verifica se a pasta existe, se não, cria ela
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# URL do vídeo
url = "https://www.youtube.com/watch?v=I8j7XJxew7s&list=RDI8j7XJxew7s&start_radio=1&pp=ygUJamF6eiBjb3J5oAcB"

# Caminho para o FFmpeg (ajuste conforme a instalação do FFmpeg)
caminho_ffmpeg = r"C:\ffmpeg\bin"  # Ajuste o caminho conforme necessário

# Opções de download
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',
    'ffmpeg_location': caminho_ffmpeg,  # Especifica o caminho do FFmpeg
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# Baixa o áudio
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
