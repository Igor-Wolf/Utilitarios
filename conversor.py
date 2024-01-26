import ffmpeg
import deletarArquivo
import verificador
import os

def converttoaudio(title):
    video_path = f"{title}.mp4"
    mp3_path = f"{title}.mp3"
    verificador.verificacao1(video_path)
    
    # Define a variável de ambiente FFMPEG_PATH para apontar para o diretório do executável do ffmpeg
    os.environ["FFMPEG_PATH"] = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")

    (
        ffmpeg.input(video_path)
        .output(mp3_path)
        .run()
    )

    print("Conversão concluída!")

    deletarArquivo.deletar_arquivo(video_path)


def convertmanual():
    
    def limpatela():
        input("\nPressione qualquer tecla para continuar...\n\n")
        os.system('cls')

    def cb():
        print("=" * 70)

    def cb0():
        cb()
        print(" " * 25 + "CONVERSOR PADRÃO" )
        cb()


    while True:
        
        limpatela()
        cb0()
        print("Qual operação deseja efetuar? \n")
        auxiliar=input('''[1] Converter arquivos existentes
[0] Sair\n\n''')
        

        if auxiliar=="1":
            video_path = input("Digite o nome do arquivo de entrada e sua extensão como no exemplo video.mp4:    ")
            mp3_path = input("Digite o nome do arquivo de saida e sua extensão como no exemplo audio.mp4:    ")
            
            # Define a variável de ambiente FFMPEG_PATH para apontar para o diretório do executável do ffmpeg
            os.environ["FFMPEG_PATH"] = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")

            (
                ffmpeg.input(video_path)
                .output(mp3_path)
                .run()
            )

            print("Conversão concluída!")
        elif auxiliar=="0":
            break
        else:
            print("Valor Incorreto")


        
