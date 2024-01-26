# Utilitáiros Change Log v. 0.4
Esse projeto tem como objetivo a elaboração de um programa que possui um conjunto de funcões utilitarias com base no ffmpeg com comandos em python para manipular arquivos como mp4, mp4, wav, jpeg, png, etc, baixar arquivos do youtube dentre outras funções. Programa ainda está em desenvolvimento. Os testes e o desenvolvimento do programa foram realizados no sistema operacional windows pelo Visual Studio Code em Python. O programa não possui fins lucrativos, é apenas para uso pessoal e fins didáticos

## Sobre o desenvolvimento

Atualmente foram utilizadas diversas biliotecas do python como ffmpeg, pythube, dentre outras. Os autores de suas respectivas bibliotecas tiveram grande importância na elaboração deste programa. Em especial vale citar o software FFMPEG que possui licença GPU - General Public Licence e pode ser conferido [aqui](https://ffmpeg.org/).
Não alterei códigos do ffmpeg apenas agreguei numa linguagem mais agradável para o usuário final poder realizar suas tarefas.
Para futuras alterações no código, tentei acessar o ffmpeg pelo executavel ffmpeg.exe contido na raiz do código, mas devido ao tamanho não consegui upá-lo no Git-Hub. Logo caso queira alterár MEU código atual, será necessario acrescentar esse executável na minha pasta raiz e ao finalizar removê-lo quando gerar o executável python.

![Organização dos Arquivos](https://github.com/Igor-Wolf/Utilitarios/blob/main/demostra%C3%A7%C3%A3o%20de%20organiza%C3%A7%C3%A3o.png?raw=true)

Para gerar o executável foi utilizada a biblioteca pyinstaller


pyinstaller --onefile meu_programa.py


## O programa de Utilitários pode ser baixado abaixo

[Utilitários](https://github.com/Igor-Wolf/Utilitarios/tree/main/dist)

## 💡 Features Added

- Programa criado com sucesso
- Adicionada uma interface para interação com o usuário através de terminal
- Adicionada a função de baixar arquivos do youtube, tanto video quanto audio
- Adicionada a função de juntar audio e video
- Adicionada a função de converter arquivos audio em video, video em audio, imagens em outros tipos de imagens (jpeg - png)
- Adicionada a função de cortar um arquivo de video ou audio

## 🕷️ Bugs Reported

- Não foram implementados testes unitários
- Não há restrição nos valores recebidos pelo usuário podendo gerar erros no sistema
- Carece de funcionalidades tipo Try/catch
- Carece de uma interface gráfica
- Dependendo do título do vídeo informado pode ocorrer erros no download, acredito que pode ser por motivo dos caracteres especiais

## 🔧 Issues Fixeds

- 

