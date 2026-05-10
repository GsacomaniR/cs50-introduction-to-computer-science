# CS50 – Aula de Memory

Este repositório contém os exercícios desenvolvidos durante a aula de Memory do curso CS50 (Introduction to Computer Science – Harvard).

Nesta etapa do curso, os principais conceitos abordados foram:

Manipulação de memória
Ponteiros
Processamento de imagens
Manipulação de arquivos binários
Estruturas de dados em baixo nível
Leitura e escrita de arquivos .bmp e .wav
# Conceitos Aprendidos

Durante a aula de Memory, foram explorados conceitos fundamentais da linguagem C relacionados ao funcionamento interno do computador e da memória.

## Principais tópicos:
Ponteiros (*)
Endereços de memória (&)
Manipulação de arrays multidimensionais
Leitura e escrita de arquivos binários
Estrutura de pixels RGB
Processamento de áudio
Algoritmos de detecção de bordas
Recuperação de arquivos apagados
Projetos Desenvolvidos
filter-less

# Projeto responsável por aplicar filtros básicos em imagens .bmp.

Filtros Implementados
Grayscale

Converte a imagem para escala de cinza utilizando a média dos valores RGB.

Conceitos utilizados:

Manipulação de pixels
Média aritmética
Estruturas RGB
Sepia

Aplica um efeito sépia à imagem utilizando fórmulas específicas para cada canal de cor.

Conceitos utilizados:

Operações matemáticas
Controle de limites (255)
Conversão de cores
Reflect

Reflete a imagem horizontalmente trocando os pixels de posição.

Conceitos utilizados:

Troca de variáveis
Percurso de arrays bidimensionais
Manipulação de memória
Blur

Aplica um efeito de desfoque calculando a média dos pixels vizinhos.

Conceitos utilizados:

Matrizes 2D
Cópia temporária da imagem
Algoritmo de suavização
filter-more

Extensão do projeto anterior, adicionando filtros mais avançados.

Edges (Sobel)

Detecta bordas da imagem utilizando o algoritmo de Sobel.

Funcionamento:

O programa aplica dois kernels matemáticos:

Gx → detecta mudanças horizontais
Gy → detecta mudanças verticais

Depois calcula a intensidade da borda usando:

sqrt(Gx² + Gy²)

Conceitos utilizados:

Convolução
Processamento digital de imagens
Matrizes matemáticas
Algoritmo de Sobel
Função sqrt()
recover

Programa responsável por recuperar imagens JPEG apagadas de um cartão de memória forense.

Funcionamento

O programa:

Lê o arquivo em blocos de 512 bytes
Identifica assinaturas JPEG
Cria novos arquivos .jpg
Reconstrói as imagens recuperadas
Conceitos utilizados
Manipulação de arquivos binários
Leitura com fread()
Escrita com fwrite()
Uso de ponteiros para arquivos (FILE *)
Estrutura de blocos de memória
Recuperação de dados
volume

Programa que modifica o volume de arquivos .wav.

Funcionamento

O programa:

Copia o cabeçalho do arquivo .wav
Lê cada amostra de áudio
Multiplica a amplitude por um fator definido pelo usuário
Gera um novo arquivo com volume alterado
Conceitos utilizados
Manipulação de áudio
Arquivos binários
Cabeçalhos WAV
Tipos inteiros (int16_t)
Conversão de dados
