# Projeto de Compressão de Imagens

## 1. Sobre o Projeto
Este projeto consiste no desenvolvimento de uma aplicação prática (Software) voltada à compressão de imagens, desenvolvido no âmbito da disciplina de Computação Visual na Universidade Presbiteriana Mackenzie. O problema central que motiva esta ferramenta é a necessidade de reduzir o tamanho de ficheiros de imagem, facilitando o seu armazenamento e partilha.

**Tema:** Compressão de Imagens
**Categoria:** Opção 4 - Aplicação Prática (Software)

## 2. Integrantes
- Rafael Moutinho Tessarotto (RA: 10395682)
- Mateus Teles Magalhães (RA: 10427410)
- Gabriel Erick Mendes (RA: 10420391)

## 3. Escopo e Funcionamento
O funcionamento da aplicação é baseado em duas informações fundamentais fornecidas pelo utilizador:
- A imagem original de entrada.
- O tamanho máximo desejado para o arquivo final (inferior ao tamanho original).

A partir dessas entradas, a ferramenta realizará um processo de compressão automático através de um algoritmo de busca binária. O resultado será uma nova versão da imagem, otimizada para atingir o tamanho limite definido, enquanto mantém a maior qualidade visual possível. 

O projeto também abrange análises e testes práticos para avaliar a relação direta entre o tamanho final atingido e a qualidade visual da imagem resultante.

## 4. Entregáveis
Ao final do desenvolvimento, são disponibilizados neste repositório:
- O código-fonte da aplicação.
- Os ficheiros necessários para a compilação do projeto.
- Uma versão executável do software pronta para uso.

## 5. Tecnologias Utilizadas
- **Linguagem de Programação:** Python
- **Bibliotecas/Ferramentas:** 
  - `Pillow` (Processamento e compressão das matrizes de imagem)
  - `Tkinter` (Criação da interface gráfica do utilizador)
  - `PyInstaller` (Empacotamento e geração do binário executável)

## 6. Como Executar

Baixe o executável disponível em "Releases" na barra direita do GitHub. O .exe já está pronto para rodar em máquinas Windows.
