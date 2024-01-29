import os
import sys

def deletar_arquivo(nome_arquivo):
    # Obtém o caminho absoluto do diretório onde o executável está localizado
    caminho_executavel = os.path.dirname(sys.argv[0])
    
    # Junta o caminho do diretório do executável com o nome do arquivo
    caminho_arquivo = os.path.join(caminho_executavel, nome_arquivo)
    print(caminho_arquivo)
    try:
        os.remove(caminho_arquivo)
        print(f"Arquivo {nome_arquivo} deletado com sucesso.")
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado em {caminho_arquivo}.")
    except Exception as e:
        print(f"Ocorreu um erro ao deletar o arquivo: {e}")

