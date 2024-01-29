import ffmpeg
import deletarArquivo
import verificador
import os


def juntarvideoeaudio(title,nome):
    video_path = f"{title}.mp4"
    mp3_path = f"{title}.mp3"
    final_path = f"{nome}1.mp4"

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



def juntarvideoeaudiomanualmente():
    
    def limpatela():
        input("\nPressione qualquer tecla para continuar...\n\n")
        os.system('cls')

    def cb():
        print("=" * 70)

    def cb0():
        cb()
        print(" " * 25 + "Junção de Arquivos" )
        cb()
    
    
    limpatela()
    cb0()
    
    video_path = input("Digite o nome do arquivo de video que deseja juntar e suas extensão (video.mp4):    ")
    mp3_path = input("Digite o nome do arquive de audio que deseja juntar como no exemplo (audio.mp3):    ")
    final_path = input("Digite o nome do arquivo de saída e sua extensão como no exemplo (video1.mp4):    ")

    verificador.verificacao3(video_path, mp3_path)
    
    # Define a variável de ambiente FFMPEG_PATH para apontar para o diretório do executável do ffmpeg
    os.environ["FFMPEG_PATH"] = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")

    video = ffmpeg.input(video_path)
    audio = ffmpeg.input(mp3_path)
    
    (
        ffmpeg.output(video, audio, final_path, vcodec='copy', acodec='aac', strict='experimental')
        .run()  # Agora o módulo ffmpeg irá procurar o executável no diretório especificado pela variável de ambiente FFMPEG_PATH
    )

    print("Junção concluída!")
