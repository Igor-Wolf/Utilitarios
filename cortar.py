import ffmpeg
import os


def cutvideo():
    
    def limpatela():
        input("\nPressione qualquer tecla para continuar...\n\n")
        os.system('cls')

    def cb():
        print("=" * 70)

    def cb0():
        cb()
        print(" " * 25 + "Download de Arquivos" )
        cb()

    limpatela()
    cb0()

    start_time = input('Digite o começo do video como no exemplo HH:MM:SS:    ') 
    end_time = input('Digite o final do video como no exemplo HH:MM:SS:    ') 

    nome = input("Digite o nome do arquivo e sua extenção como no exemplo video.mp4:    ")
    saida = input("Digite o nome do arquivo e sua extenção como no exemplo video.mp4:    ")

    # Define a variável de ambiente FFMPEG_PATH para apontar para o diretório do executável do ffmpeg
    os.environ["FFMPEG_PATH"] = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")

    (
        ffmpeg.input(nome, ss=start_time, to=end_time)
        .output(saida)
        .run()
    )
