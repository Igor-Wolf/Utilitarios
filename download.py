from pytube import YouTube
from PyQt6 import QtWidgets, QtGui, QtCore

import requests
from PIL import Image
import merge
import conversor
import rename
import deletarArquivo


def checagem(url, textotitulo, imagem, opcao, info, auxiliar):
    try:
        yt = YouTube(url)
        textotitulo.setText(f'Título: {yt.title}')
        info.setText("Info: Checando Vídeo")

        if auxiliar == "1":
            try:
                #print("\n Listar Formatos em MP4")
                opcao.clear()

                for item in yt.streams.filter(file_extension='mp4', type="video"):
                    # print(item)
                    if item.itag == 137:
                        opcao.addItem("1080p")
                        #print(item)
                        info.setText("Info: Vídeo encontrado")
                    elif item.itag == 136:
                        opcao.addItem("720p")
                        #print(item)
                        info.setText("Info: Vídeo encontrado")
                    elif item.itag == 135:
                        opcao.addItem("480p")
                        #print(item)
                        info.setText("Info: Vídeo encontrado")
                    elif item.itag == 134:
                        opcao.addItem("360p")
                        #print(item)
                        info.setText("Info: Vídeo encontrado")
                    elif item.itag == 133:
                        opcao.addItem("240p")
                        #print(item)
                        info.setText("Info: Vídeo encontrado")
                    elif item.itag == 160:
                        opcao.addItem("144p")
                        #print(item)
                        info.setText("Info: Vídeo encontrado")
            except:
                info.setText("Info: Vídeo não encontrado")
                #print("\n")
        elif auxiliar == "2":
            try:
                #print("\n Listar Formatos em Audio")
                opcao.clear()

                for item in yt.streams.filter(only_audio=True):
                    #print(item)

                    if item.itag == 139:
                        opcao.addItem("48kbps")
                        #print(item)
                        info.setText("Info: Vídeo encontrado")
                    elif item.itag == 140:
                        opcao.addItem("128kbps")
                        #print(item)
                        info.setText("Info: Vídeo encontrado")
            except:
                info.setText("Info: Vídeo não encontrado")

        elif auxiliar == "3":
            texto=""
            for item in yt.streams:
                texto = f"{texto}{item}\n"
                info.setText(texto)
                #print(item)
                #print("\n")
        else:
            pass
        
        # Faz a requisição GET para o URL da imagem
        response = requests.get(yt.thumbnail_url)
        # Verifica se a requisição foi bem-sucedida (status code 200)
        if response.status_code == 200:
            # Salva os dados da imagem em um arquivo temporário
            with open('temp/temp_image.jpg', 'wb') as f:
                f.write(response.content)
                # Abre a imagem temporária usando o PyQt6
                pixmap = QtGui.QPixmap('temp/temp_image.jpg')
                # Exibe a imagem no QLabel
                pixmap = pixmap.scaled(imagem.size().width(), imagem.size().height(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
                imagem.setPixmap(pixmap)
                imagem.setScaledContents(True)  # Escala a imagem para o tamanho do QLabel
        else:
            #print(f"Falha ao exibir a imagem. Status code: {response.status_code}")
             pass        
            
    except Exception as e:
        #print(f"Ocorreu um erro ao exibir a imagem: {e}")
        try:
            deletarArquivo.deletar_arquivo("temp/temp_image.jpg")
            imagem.clear()
            textotitulo.clear()
            opcao.clear()
            info.clear()
        except:
            info.setText("Info: Vídeo não encontrado")

def downloadmanual(auxiliar,url, opcao,caminho, info):

    if auxiliar=="1":
            try:
               yt = YouTube(url)#inserir a URL do video
               
               nome=yt.title
               yt.title="arquivo"
               

               if yt.streams.filter(type="video"):
                    
                    info.setText("Info: Iniciando Download de arquivos de audio")
                    stream = yt.streams.get_by_itag(140)
                    #print(stream)
                    stream.download("temp")
                    info.setText("Info: Formatando arquivos de video")
                    info.setText("Info: Convertendo arquivos de audio")
                    conversor.converttoaudio(yt.title, f"temp/{yt.title}.mp3")

               if opcao=="144p":
                    escolha="160"
                    stream = yt.streams.get_by_itag(escolha)
                    #print(stream)
                    stream.download("temp")
                    info.setText("Info: Formatando arquivos de video")
                    merge.juntarvideoeaudio(yt.title, nome, caminho)
                    info.setText("Info: Arquivo baixado com sucesso")
                    
               elif opcao=="240p":
                    escolha="133"
                    stream = yt.streams.get_by_itag(escolha)
                    #print(stream)
                    stream.download("temp")
                    info.setText("Info: Formatando arquivos de video")
                    merge.juntarvideoeaudio(yt.title, nome, caminho) 
                    info.setText("Info: Arquivo baixado com sucesso")                
                    
               elif opcao=="360p":
                    escolha="134"
                    stream = yt.streams.get_by_itag(escolha)
                    #print(stream)
                    stream.download("temp")
                    info.setText("Info: Formatando arquivos de video")
                    merge.juntarvideoeaudio(yt.title, nome, caminho)
                    info.setText("Info: Arquivo baixado com sucesso")                 
                    
               elif opcao=="480p":
                    escolha="135"
                    stream = yt.streams.get_by_itag(escolha)
                    #print(stream)
                    stream.download("temp")
                    info.setText("Info: Formatando arquivos de video")
                    merge.juntarvideoeaudio(yt.title, nome, caminho)
                    info.setText("Info: Arquivo baixado com sucesso")
                    
               elif opcao=="720p":
                    escolha="136"
                    stream = yt.streams.get_by_itag(escolha)
                    #print(stream)
                    stream.download("temp")
                    info.setText("Info: Formatando arquivos de video")
                    merge.juntarvideoeaudio(yt.title, nome, caminho)
                    info.setText("Info: Arquivo baixado com sucesso")
                    
               elif opcao=="1080p":
                    info.setText("Info: Iniciando Download de arquivos de video")
                    escolha="137"
                    stream = yt.streams.get_by_itag(escolha)
                    #print(stream)
                    stream.download("temp")
                    info.setText("Info: Formatando arquivos de video")
                    merge.juntarvideoeaudio(yt.title, nome, caminho)
                    info.setText("Info: Arquivo baixado com sucesso")
                    
               elif opcao=="4k":
                    pass
               elif opcao=="8k":
                    pass
            except:
               info.setText("Info: Vídeo não encontrado")


    elif auxiliar=="2":

          try:
               
               yt = YouTube(url)#inserir a URL do video
               #nome=yt.title

               if opcao=="48kbps":
                         escolha="139"
                         stream = yt.streams.get_by_itag(escolha)
                         #print(stream)
                         stream.download("temp")
                         info.setText("Info: Convertendo arquivos de audio")
                         conversor.converttoaudio(yt.title,caminho)
                         rename.renomear_arquivo(yt.title, caminho)
                         
               
               
               elif opcao=="128kbps":                         
                         escolha="140"
                         stream = yt.streams.get_by_itag(escolha)
                         #print(stream)
                         stream.download("temp")
                         info.setText("Info: Convertendo arquivos de audio")
                         conversor.converttoaudio(yt.title, caminho)
                         rename.renomear_arquivo(yt.title, caminho)
          except:
               info.setText("Info: Vídeo não encontrado")

    elif auxiliar=="3":
        try:
            yt = YouTube(url)#inserir a URL do video
            escolha = int(opcao)

            stream = yt.streams.get_by_itag(escolha)
            #print(stream)
            stream.download(caminho)
            info.setText("Info: Arquivo baixado com sucesso")
        except:
             info.setText("Info: Vídeo não encontrado")

    else:
        pass