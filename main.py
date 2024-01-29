import download
import os
import conversor
import cortar
import gravartela
import merge

#================================================================== CABEÇALHOS

def limpatela():
    input("\nPressione qualquer tecla para continuar...\n\n")
    os.system('cls')

def cb():
    print("=" * 70)

def cb0():
    cb()
    print(" " * 25 + "PROGRAMA DE UTILITÁRIOS" )
    cb()

#================================================================== PROGRAMA PRINCIPAL

os.system('cls')
while True:

    cb0()
    print("Qual operação deseja efetuar? \n")
    auxiliar=input('''[1] Download de arquivos
[2] Conversor de arquivos
[3] Edição de arquivos
[4] Realizar gravação
[5] Juntar vídeo e audio                   
[0] Sair\n\n''')


    if auxiliar== "1":
        try:
            download.downloadmanual()
            limpatela()
        except:
            print("Erro, operação encerrada!")
    elif auxiliar== "2":
        try:
            conversor.convertmanual()
            limpatela()
        except:
            print("Erro, operação encerrada!")
    elif auxiliar=="3":
        try:
            cortar.cutvideo()
            limpatela()
        except:
            print("Erro, operação encerrada!")
    elif auxiliar =="4":
        try:
            gravartela.gravar()
        except:
            print("Erro, operação encerrada!")
    elif auxiliar =="5":
        try:
            merge.juntarvideoeaudiomanualmente()
        except:
            print("Erro, operação encerrada!")
    elif auxiliar=="0":
        break
    else: 
        print("Digito inválido")