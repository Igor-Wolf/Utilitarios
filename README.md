# Utilitáiros GUI (Graphical User Interface) Change Log v. 0.5 (Defasado devido às atualizações do youtube)
Esse projeto tem como objetivo a elaboração de um programa que possui um conjunto de funcões utilitarias com base no ffmpeg com comandos em python para manipular arquivos como mp4, mp3, wav, jpeg, png, etc, baixar arquivos do youtube dentre outras funções. Programa ainda está em desenvolvimento. Os testes e o desenvolvimento do programa foram realizados no sistema operacional windows pelo Visual Studio Code em Python. O programa não possui fins lucrativos, é apenas para uso pessoal e fins didáticos

## Sobre o desenvolvimento

Atualmente foram utilizadas diversas biliotecas do python como ffmpeg, pythube, dentre outras. Os autores de suas respectivas bibliotecas tiveram grande importância na elaboração deste programa. Em especial vale citar o software FFMPEG que possui licença GPU - General Public Licence e pode ser conferido [aqui](https://ffmpeg.org/).
Não alterei códigos do ffmpeg apenas agreguei numa linguagem mais agradável para o usuário final poder realizar suas tarefas.
Para futuras alterações no código, houve a tentativa de acessar o ffmpeg pelo executavel ffmpeg.exe contido na raiz do código, mas devido ao tamanho não foi possível upá-lo no Git-Hub. Logo caso haja a necessidade de alterar o código atual, será preciso  acrescentar esse executável na pasta raiz e ao finalizar (depois do deploy) removê-lo quando gerar o executável python.

![Organização dos Arquivos](https://github.com/Igor-Wolf/Utilitarios/blob/GUI/organiza%C3%A7%C3%A3o%20dos%20arquivos.png?raw=true)

Para gerar o executável foi utilizada a biblioteca pyinstaller:

pyinstaller.exe --onefile --windowed --icon=favicon.ico main.py



## O programa de Utilitários pode ser baixado abaixo


- Programa completo para funcionamento

[Utilitários Completo](https://mega.nz/file/wLJ13RDJ#1OelFMnbu-beANzY7wFrjUQ1gkeW-FiD9VVGHH6fSjE)

Para realizar o funcionamento basta baixar o arquivo e executar o instalador

## Modo de Usar

Realizada a instalação através do instalador já será possivel realizar todas as operações que o programa proporciona
Execute o arquivo em MODO ADMINISTRADOR para evitar erros de permissões.

![Tela de Início](https://github.com/Igor-Wolf/Utilitarios/blob/GUI/programa%20rodando.png?raw=true)

Todas as operações feitas criarão arquivos na mesma raiz onde se encontram tanto o utilitarios.exe quanto ffmpeg.exe. Logo se escolher a função download de arquivos, por exemplo, o video.mp4 será criado nessa pasta.
No que diz respeito às funcionalidades é possível dizer o seguinte:

- Download: Aqui você conseguirá baixar tanto videos, quanto audios do youtube. É importante lembrar que o youtube organiza os arquivos de maneira diferenciada. Ele separa o que você exerga e o que você escuta em arquivos diferentes. Foram definidas três sub opções para o usuário escolher sendo elas download de videos (aplicando-se o filtro video/mp4), download de audios (aplicando-se o filtro audio/mp4), e download de arquivos diversos (que não leva em consideração filtros). Após a escolha da opção o usuário deverá indicar qual itag deseja baixar, para videos é recomendada a 137 que possui maior qualidade, já o audio a 140.

- Conversão: Nessa opção o usuário poderá converter arquivos em outros formatos, em espeicial .mp4 em .mp3. É possivel também converter arquivos de imagens em outros tipos como png - jpg ou mesmo webP - jpeg basta indicar o nome e a extensão do arquivo.

- Edição: É uma opção bastante rudimentar para realizar cortes em arquivos de audio e video. Nela você poderá indicar o tempo de início e final do vídeo que desejá realizar o corte

- Gravar: Um protótipo da funcionálidade de gravar tela, nela é possivel gravar a tela até o usuário digitar ctrl+c no terminal. Lembrando que por ser um protótipo apenas a tela será gravada, não contendo nenhum áudio captado junto à imagem.

- Junção: Essa opção é feita para mesclar arquivos de video, em especial que não possuem audio, ao seu respectivo audio.

## 💡 Features Added

- Programa criado com sucesso
- Adicionada uma interface para interação com o usuário através de terminal
- Adicionada a função de baixar arquivos do youtube, tanto video quanto audio
- Adicionada a função de juntar audio e video
- Adicionada a função de converter arquivos audio em video, video em audio, imagens em outros tipos de imagens (jpeg - png)
- Adicionada a função de cortar um arquivo de video ou audio
- Adicionada funcionalidades tipo Try/catch
- Adicionada a funcionalidade de gravar a tela
- Adicionada interface gráfica

## 🕷️ Bugs Reported

- Não foram implementados testes unitários
- Não há restrição nos valores recebidos pelo usuário podendo gerar erros no sistema



## 🔧 Issues Fixeds

-  Dependendo do título do vídeo informado pode ocorrer erros no download, provavelmente por motivo dos caracteres especiais

