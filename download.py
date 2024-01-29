from pytube import YouTube
import merge
import conversor
import os
import rename


def downloadmanual():

    def limpatela():
        input("\nPressione qualquer tecla para continuar...\n\n")
        os.system('cls')

    def cb():
        print("=" * 70)

    def cb0():
        cb()
        print(" " * 25 + "Download de Arquivos" )
        cb()


    while True:
        
        limpatela()
        cb0()
        print("Qual operação deseja efetuar? \n")
        auxiliar=input('''[1] Download de videos do youtube
[2] Download de audios do youtube
[3] download de arquivos diversos do youtube
[0] Sair\n\n''')
        
        
        
        if auxiliar=="1":
            yt = YouTube(input('Cole a URL do video: \n'))#inserir a URL do video
            
            print(yt.title) #mostra o título do video
            nome=yt.title
            print("\n Thumbnail")
            print(yt.thumbnail_url) #mostra o link da thumbnail do video
            yt.title="arquivo"
            print("\n Listar Formatos em MP4")

            for item in yt.streams.filter(file_extension='mp4', type="video"):
                
               
                print(item)
                print("\n")

            escolha = int(input("\nQual itag deseja baixar? "))


            if yt.streams.filter(type="video"):
                
                stream = yt.streams.get_by_itag(140)
                print(stream)
                stream.download()
                conversor.converttoaudio(yt.title)

            stream = yt.streams.get_by_itag(escolha)
            print(stream)
            stream.download()
            merge.juntarvideoeaudio(yt.title, nome)
            


        elif auxiliar=="2":

            yt = YouTube(input('Cole a URL do video: \n'))#inserir a URL do video
            nome=yt.title
            print(yt.title) #mostra o título do video

            print("\n Thumbnail")
            print(yt.thumbnail_url) #mostra o link da thumbnail do video
            yt.title="arquivo"

            print("\n\n Listar Formatos em audio")

            for item in yt.streams.filter(only_audio=True):
                print(item)
                print("\n")


            escolha = int(input("\n\nQual itag deseja baixar? "))


            stream = yt.streams.get_by_itag(escolha)
            print(stream)
            stream.download()

            conversor.converttoaudio(yt.title)
            nome= nome+"1.mp3"
            rename.renomear_arquivo(yt.title, nome)

            
        elif auxiliar=="3":

            yt = YouTube(input('Cole a URL do video: \n'))#inserir a URL do video
            print(yt.title) #mostra o título do video

            print("\n Thumbnail")
            print(yt.thumbnail_url) #mostra o link da thumbnail do video
            #yt.title="arquivo"
            print("\n Listar Formatos")

            for item in yt.streams:
                print(item)
                print("\n")

            escolha = int(input("\n\nQual itag deseja baixar? "))

            stream = yt.streams.get_by_itag(escolha)
            print(stream)
            stream.download()

        elif auxiliar=="0":
            break
        else:
            print("Valor Incorreto!")

                
        
    
