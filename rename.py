import os
import sys

def get_directory():
    # Obtém o diretório do script Python ou do executável final
    if getattr(sys, 'frozen', False):
        # Executável final
        diretorio = os.path.dirname(sys.executable)
    elif __file__:
        # Script Python
        diretorio = os.path.dirname(__file__)
    else:
        # Caso não seja possível determinar o diretório
        diretorio = os.getcwd()
    return diretorio

def renomear_arquivo(nome_antigo, nome_novo):
    nome_antigo=nome_antigo+".mp3"
    
    try:
        # Obtém o diretório onde o executável está localizado
        diretorio_executavel = get_directory()
        
        # Junta o diretório com os nomes dos arquivos antigo e novo
        caminho_antigo = os.path.join(diretorio_executavel, nome_antigo)
        caminho_novo = os.path.join(diretorio_executavel, nome_novo)
        
        os.rename(caminho_antigo, caminho_novo)
        print(f"Arquivo renomeado de {nome_antigo} para {nome_novo} com sucesso.")
    except FileNotFoundError:
        print(f"O arquivo {nome_antigo} não foi encontrado.")
        print(caminho_antigo)
    except FileExistsError:
        print(f"O arquivo {nome_novo} já existe.")
    except Exception as e:
        print(f"Ocorreu um erro ao renomear o arquivo: {e}")

# Testando a função renomear_arquivo com um exemplo
renomear_arquivo("arquivo_antigo.txt", "arquivo_novo.txt")
