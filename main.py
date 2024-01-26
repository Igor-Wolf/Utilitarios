import download
import os
import conversor
import cortar
import gravartela

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
[0] Sair\n\n''')


    if auxiliar== "1":
        download.downloadmanual()
        limpatela()
    elif auxiliar== "2":
        conversor.convertmanual()
        limpatela()
    elif auxiliar=="3":
        cortar.cutvideo()
        limpatela()
    elif auxiliar =="4":
        gravartela.gravar()
    elif auxiliar=="0":
        break
    else: 
        print("Digito inválido")