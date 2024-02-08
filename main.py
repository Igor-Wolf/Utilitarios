import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QEasingCurve
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QLabel



from pytube import YouTube
import download
import merge
import conversor
import cortar
import gravartela


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("igrafica.ui", self) #NOME DO ARQUIVO .ui para ser convertido dinamicamente
        self.setWindowTitle("Utilitários")
        self.setWindowIcon(QIcon("icons/favicon.ico"))
        label = self.logo
        label.setText('<html><body><p align="center"><img src="icons/ferramentas.png"/></p><p align="center"><span style=" font-size:16pt; font-style:italic;">© Utilitários </span></p></body></html>')
        label.show()

    #====================================================================================================BOTÕES


        self.icon.clicked.connect(self.left_menu)
        self.home.clicked.connect(self.mudar_home)
        self.download.clicked.connect(self.mudar_download)
        self.conversao.clicked.connect(self.mudar_conversao)
        self.edicao.clicked.connect(self.mudar_edicao)
        self.juncao.clicked.connect(self.mudar_juncao)
        self.gravacao.clicked.connect(self.mudar_gravacao)
        

        self.checkButton.clicked.connect(self.checar_url)
        self.downloadButton.clicked.connect(self.executar_download)

        self.checkButton_audio.clicked.connect(self.checar_url_audio)
        self.downloadButton_audio.clicked.connect(self.executar_download_audio)

        self.checkButton_diversos.clicked.connect(self.checar_url_diversos)
        self.downloadButton_diversos.clicked.connect(self.executar_download_diversos)

        self.selecionarconversor1.clicked.connect(self.selecionar_arquivo1)
        self.selecionarconversor2.clicked.connect(self.selecionar_arquivo2)
        self.convert.clicked.connect(self.converter)

        self.selecionarcorte1.clicked.connect(self.selecionar_arquivo1_corte)
        self.selecionarcorte2.clicked.connect(self.selecionar_arquivo2_corte)
        self.cut.clicked.connect(self.cortar)

        self.selecionarjuncao1.clicked.connect(self.selecionar_arquivo1_juncao)
        self.selecionarjuncao2.clicked.connect(self.selecionar_arquivo2_juncao)
        self.selecionarjuncao3.clicked.connect(self.selecionar_arquivo3_juncao)
        self.merge.clicked.connect(self.juntar)

        self.selecionargravar.clicked.connect(self.selecionar_arquivo1_gravar)
        self.gravar.clicked.connect(self.screenrecorder)
        #self.parar.clicked.connect(self.screenrecorderstop)
       


  #====================================================================================================MENU LATERAL            
    
    def left_menu(self):
        width = self.left_Menu.width()

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QtCore.QPropertyAnimation(self.left_Menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)

        # Define uma curva de easing personalizada usando uma função lambda
        easing_curve = QtCore.QEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)

        self.animation.setEasingCurve(easing_curve)

        self.animation.start()



    def mudar_home(self):
        self.principal.setCurrentIndex(0)
        self.title_label.setText("BEM VINDO")

    def mudar_download(self):
        self.principal.setCurrentIndex(1)
        self.title_label.setText("DOWNLOAD")

    def mudar_conversao(self):
        self.principal.setCurrentIndex(2)
        self.title_label.setText("CONVERSÃO")

    def mudar_edicao(self):
        self.principal.setCurrentIndex(3)
        self.title_label.setText("EDIÇÃO")

    def mudar_juncao(self):
        self.principal.setCurrentIndex(4)
        self.title_label.setText("JUNÇÃO")
        
    def mudar_gravacao(self):
        self.principal.setCurrentIndex(5)
        self.title_label.setText("GRAVAÇÃO")

    


   #====================================================================================================DOWNLOAD   
    
    def checar_url(self):
        
        download.checagem(self.urltext_imput.text(), self.textimage_label, self.imagem_label, self.optionsBox, self.info_label,"1")
    
    def checar_url_audio(self):
        
        download.checagem(self.urltext_imput_audio.text(), self.textimage_label_audio, self.imagem_label_audio, self.optionsBox_audio, self.info_label_audio,"2")

    def checar_url_diversos(self):
        
        download.checagem(self.urltext_imput_diversos.text(), self.textimage_label_diversos, self.imagem_label_diversos, self.optionsBox_audio, self.info_label_diversos,"3")

    def executar_download(self):

        file_name, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivos", "", "All Files (*);;Video Files (*.mp4)")
                      
        if file_name:
            #print("Selected File:", file_name)
    
            download.downloadmanual("1",self.urltext_imput.text(),self.optionsBox.currentText(),file_name, self.info_label)

    def executar_download_audio(self):
        
        file_name, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivos", "", "All Files (*);;Audio Files (*.mp3)")
                      
        if file_name:
            #print("Selected File:", file_name)
    
            download.downloadmanual("2",self.urltext_imput_audio.text(),self.optionsBox_audio.currentText(),file_name, self.info_label_audio)

    def executar_download_diversos(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivos", "", "All Files (*)")
                      
        if file_name:
            #print("Selected File:", file_name)
    
            download.downloadmanual("3",self.urltext_imput_diversos.text(),self.lineEdit_diversos.text(),file_name, self.info_label_diversos)


    #====================================================================================================CONVERSÃO 
            
    def selecionar_arquivo1(self):
        
        file_name, _ = QFileDialog.getOpenFileName(self, "Salvar Arquivos", "", "All Files (*);;Video Files (*.mp4);;Audio Files (*.mp3)")

        self.caminhoconversor1.setText(file_name)

    def selecionar_arquivo2(self):
        
        file_name, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivos", "", "All Files (*);;Video Files (*.mp4);;Audio Files (*.mp3)")

        self.caminhoconversor2.setText(file_name)

    def converter(self):

        if self.caminhoconversor1.text() and self.caminhoconversor2.text():

            try:
                conversor.convertmanual(self.caminhoconversor1.text(), self.caminhoconversor2.text())
                self.infoconversor.setText("Info: Conversão realizada com sucesso")
            except:
                self.infoconversor.setText("Info: Não foi possível realizar a conversão dos arquivos")  
        else:
            self.infoconversor.setText("Info: Selecione o caminho dos arquivos")   
        
    #====================================================================================================CORTE
            
    def selecionar_arquivo1_corte(self):
        
        file_name, _ = QFileDialog.getOpenFileName(self, "Salvar Arquivos", "", "All Files (*);;Video Files (*.mp4);;Audio Files (*.mp3)")

        self.caminhocorte1.setText(file_name)

    def selecionar_arquivo2_corte(self):
        
        file_name, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivos", "", "All Files (*);;Video Files (*.mp4);;Audio Files (*.mp3)")

        self.caminhocorte2.setText(file_name)

    def cortar(self):

        if self.caminhocorte1.text() and self.caminhocorte2.text() and self.time1.text() and self.time2.text():

            try:
                cortar.cutvideo(self.caminhocorte1.text(), self.caminhocorte2.text(), self.time1.text(), self.time2.text())
                self.infocorte.setText("Info: Corte realizado com sucesso")
            except:
                self.infocorte.setText("Info: Não foi possível realizar o corte dos arquivos")  
        else:
            self.infocorte.setText("Info: Selecione o caminho e o tempo dos arquivos")   

#====================================================================================================JUNÇÃO
            
    def selecionar_arquivo1_juncao(self):
        
        file_name, _ = QFileDialog.getOpenFileName(self, "Salvar Arquivos", "", "All Files (*);;Video Files (*.mp4);;Audio Files (*.mp3)")

        self.caminhojuncao1.setText(file_name)

    def selecionar_arquivo2_juncao(self):
        
        file_name, _ = QFileDialog.getOpenFileName(self, "Salvar Arquivos", "", "All Files (*);;Video Files (*.mp4);;Audio Files (*.mp3)")

        self.caminhojuncao2.setText(file_name)

    def selecionar_arquivo3_juncao(self):
        
        file_name, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivos", "", "All Files (*);;Video Files (*.mp4);;Audio Files (*.mp3)")

        self.caminhojuncao3.setText(file_name)


    def juntar(self):

        if self.caminhojuncao1.text() and self.caminhojuncao2.text() and self.caminhojuncao3.text():

            try:
                merge.juntarvideoeaudiomanualmente(self.caminhojuncao1.text(), self.caminhojuncao2.text(), self.caminhojuncao3.text())
                self.infojuncao.setText("Info: Junção realizada com sucesso")
            except:
                self.infojuncao.setText("Info: Não foi possível realizar a junção dos arquivos")  
        else:
            self.infojuncao.setText("Info: Selecione o caminho dos arquivos")

    #====================================================================================================JUNÇÃO

    def selecionar_arquivo1_gravar(self):
        
        file_name, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivos", "", "All Files (*);;Video Files (*.mp4);;Audio Files (*.mp3)")

        self.caminhogravar.setText(file_name)

   

    def screenrecorder(self):
        if self.caminhogravar.text():
            try:
                self.infogravar.setText("Info: Gravação iniciada com sucesso, pressione a tecla 'q' para encerrar a gravação")
                gravartela.gravar(self.caminhogravar.text())                
            except Exception as e:
                self.infogravar.setText(f"Info: Não foi possível iniciar a gravação - {e}")
        else:
            self.infogravar.setText("Info: Selecione o caminho dos arquivos")

    # def screenrecorderstop(self):
    #     try:
    #         gravartela.parargravacao()
    #         self.infogravar.setText("Info: Gravação interrompida com sucesso")
    #     except Exception as e:
    #         self.infogravar.setText(f"Info: Não foi possível interromper a gravação - {e}")
    #         print(f"Info: Não foi possível interromper a gravação - {e}")

       
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

