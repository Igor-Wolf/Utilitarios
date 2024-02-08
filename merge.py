import subprocess
import os
import deletarArquivo
import verificador

def juntarvideoeaudio(title, nome, caminho):
    video_path = f"temp/{title}.mp4"
    mp3_path = f"temp/{title}.mp3"
    final_path = caminho

    verificador.verificacao2(video_path, mp3_path)

    ffmpeg_command = [
        "ffmpeg",
        "-i", video_path,            # Arquivo de vídeo
        "-i", mp3_path,              # Arquivo de áudio
        "-c:v", "copy",              # Codec de vídeo (copiar sem re-encode)
        "-c:a", "aac",               # Codec de áudio (AAC)
        "-strict", "experimental",   # Opção para permitir codecs experimentais
        final_path                  # Arquivo de saída
    ]

    # Executa o comando ffmpeg de forma silenciosa
    subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print("Conversão concluída!")

    deletarArquivo.deletar_arquivo(mp3_path)
    deletarArquivo.deletar_arquivo(video_path)


def juntarvideoeaudiomanualmente(caminho1, caminho2, caminho3):
    video_path = caminho1
    mp3_path = caminho2
    final_path = caminho3

    verificador.verificacao3(video_path, mp3_path)

    ffmpeg_command = [
        "ffmpeg",
        "-i", video_path,            # Arquivo de vídeo
        "-i", mp3_path,              # Arquivo de áudio
        "-c:v", "copy",              # Codec de vídeo (copiar sem re-encode)
        "-c:a", "aac",               # Codec de áudio (AAC)
        "-strict", "experimental",   # Opção para permitir codecs experimentais
        final_path                  # Arquivo de saída
    ]

    # Executa o comando ffmpeg de forma silenciosa
    subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

