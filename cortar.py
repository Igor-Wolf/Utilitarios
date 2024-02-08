import subprocess
import os


def cutvideo(caminho1, caminho2, tempo1, tempo2):
    start_time = tempo1 
    end_time = tempo2

    nome = caminho1
    saida = caminho2

    # Define o comando ffmpeg com os parâmetros desejados
    ffmpeg_command = [
        "ffmpeg",
        "-ss", str(start_time),  # Tempo de início
        "-to", str(end_time),    # Tempo de fim
        "-i", nome,              # Arquivo de entrada
        "-c", "copy",            # Copiar os streams de áudio e vídeo sem re-encode
        saida                    # Arquivo de saída
    ]

    # Executa o comando ffmpeg de forma silenciosa
    subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
