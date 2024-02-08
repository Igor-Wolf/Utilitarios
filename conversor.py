import subprocess
import os
import deletarArquivo
import verificador

def converttoaudio(title, caminho):
    video_path = f"temp/{title}.mp4"
    mp3_path = caminho
    verificador.verificacao1(video_path)

    ffmpeg_command = [
        "ffmpeg",
        "-i", video_path,    # Arquivo de entrada (vídeo)
        mp3_path             # Arquivo de saída (áudio)
    ]

    # Executa o comando ffmpeg de forma silenciosa
    subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    deletarArquivo.deletar_arquivo(video_path)

def convertmanual(inicial, final):
    video_path = inicial
    mp3_path = final

    ffmpeg_command = [
        "ffmpeg",
        "-i", video_path,    # Arquivo de entrada (vídeo)
        mp3_path             # Arquivo de saída (áudio)
    ]

    # Executa o comando ffmpeg de forma silenciosa
    subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
