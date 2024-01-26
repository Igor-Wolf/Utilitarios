import os

def deletar_arquivo(nome_arquivo):
    caminho_arquivo = os.path.join(os.path.dirname(__file__), nome_arquivo)

    try:
        os.remove(caminho_arquivo)
        print(f"Arquivo {nome_arquivo} deletado com sucesso.")
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao deletar o arquivo: {e}")


