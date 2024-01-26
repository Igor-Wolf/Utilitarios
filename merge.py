import ffmpeg
import deletarArquivo
import verificador
import os

def juntarvideoeaudio(title):
    video_path = f"{title}.mp4"
    mp3_path = f"{title}.mp3"
    final_path = f"{title}1.mp4"

    verificador.verificacao2(video_path, mp3_path)
    
    # Define a variável de ambiente FFMPEG_PATH para apontar para o diretório do executável do ffmpeg
    os.environ["FFMPEG_PATH"] = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")

    video = ffmpeg.input(video_path)
    audio = ffmpeg.input(mp3_path)
    
    (
        ffmpeg.output(video, audio, final_path, vcodec='copy', acodec='aac', strict='experimental')
        .run()  # Agora o módulo ffmpeg irá procurar o executável no diretório especificado pela variável de ambiente FFMPEG_PATH
    )

    print("Conversão concluída!")

    deletarArquivo.deletar_arquivo(mp3_path)
    deletarArquivo.deletar_arquivo(video_path)
