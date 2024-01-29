import os
import time

def verificacao1(video_path):
# Verifica periodicamente se o arquivo mp4 existe
    while not os.path.exists(video_path):
        print(f"Aguardando o download de {video_path}...")
        time.sleep(5)  # Aguarda 5 segundos antes da próxima verificação
    print(f"Download de {video_path} verificado. Iniciando conversão...")


def verificacao2(video_path, mp3_path):
    # Verifica periodicamente se o arquivo mp4 existe
    while not os.path.exists(video_path and mp3_path):
        print(f"Aguardando o download de {video_path}...")
        time.sleep(5)  # Aguarda 5 segundos antes da próxima verificação

    print(f"Download de {video_path} e {mp3_path} concluído. Iniciando operação")

def verificacao3(video_path, mp3_path):
    # Verifica periodicamente se o arquivo mp4 existe
    if not (video_path and mp3_path):
        print(f"Arquivos não encontrados {video_path} ou {mp3_path}...")
        

    print(f"Verificação de {video_path} e {mp3_path} concluído. Iniciando operação")