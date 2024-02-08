import cv2
from vidgear.gears import ScreenGear

def gravar(caminho):
    # Define o codec de vídeo e cria o objeto VideoWriter para salvar a gravação
    output_video_filename = caminho
    codec = cv2.VideoWriter_fourcc(*"mp4v")  # Codec de vídeo (MP4)
    fps = 25.0  # Taxa de frames por segundo
    resolution = (1920, 1080)  # Resolução do vídeo (largura, altura)
    output_video = cv2.VideoWriter(output_video_filename, codec, fps, resolution)

    # Inicializa o objeto ScreenGear para capturar a tela
    screen_capturer = ScreenGear().start()

    # Variável para verificar se a janela já foi criada
    janela_criada = False

    # Loop principal para capturar e salvar os frames
    while True:
        # Captura o próximo frame da tela
        frame = screen_capturer.read()

        # Verifica se o frame é válido
        if frame is None:
            break

        # Verifica se a janela já foi criada
        if not janela_criada:
            cv2.namedWindow("Captura de Tela")
            janela_criada = True

        # Salva o frame no arquivo de vídeo
        output_video.write(frame)

        # Exibe o frame
        cv2.imshow("Captura de Tela", frame)

        # Verifica se a tecla 'q' foi pressionada para sair do loop
        if cv2.waitKey(1) & 0xFF in [ord('q'), ord('Q')]:
            break

    # Libera recursos
    cv2.destroyAllWindows()
    screen_capturer.stop()
    output_video.release()

