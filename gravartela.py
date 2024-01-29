import subprocess
import os

processo_gravacao = None

def gravar():
  

    def iniciar_gravacao(nome_arquivo_saida):
        global processo_gravacao
        comando_ffmpeg = [
            'ffmpeg',        # Executável FFmpeg
            '-f', 'gdigrab', # Formato de entrada para capturar a tela do Windows
            '-i', 'desktop', # Dispositivo de captura (desktop = tela inteira)
            nome_arquivo_saida  # Nome do arquivo de saída
        ]
       
        # Iniciar o processo FFmpeg em segundo plano
        processo_gravacao = subprocess.Popen(comando_ffmpeg)

        print("Gravação iniciada")

      
    def limpatela():
        input("\nPressione Enter para continuar...\n\n")
        os.system('cls')

    def cb():
        print("=" * 70)

    def cb0():
        cb()
        print(" " * 25 + "Realizar gravações" )
        cb()

    while True:
        limpatela()
        cb0()
        print("\n[1] Iniciar gravação")
        print("[0] Sair\n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_arquivo = input("Digite o nome do arquivo de saída (ex: video.mp4): ")
            print("Para encerrar a gravação precione Ctrl + C")
            input("Pressione enter para continuar...")
            iniciar_gravacao(nome_arquivo)

        elif opcao == "0":
            break
