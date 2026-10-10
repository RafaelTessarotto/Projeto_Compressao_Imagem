# Plano de Passo a Passo: Desenvolvimento da Aplicação

## Fase 1: Preparação do Ambiente e Tecnologias
1. **Definição da Linguagem:** Escolher a linguagem Python, que é excelente para processamento de imagens e possui ferramentas simples para gerar executáveis.
2. **Biblioteca de Imagens:** Utilizar a biblioteca `Pillow` (PIL) para manipular as imagens no código. Esta biblioteca permite abrir uma imagem, ler suas informações e salvá-la ajustando o parâmetro de `quality` (qualidade).
3. **Controle de Versão:** Criar o repositório e compartilhar com os membros do grupo (Rafael, Mateus e Gabriel).

## Fase 2: A Lógica de Compressão (O Algoritmo)
O requisito principal dita que o usuário define um tamanho máximo para o arquivo. Como a compressão em formatos como JPEG é baseada em um índice de qualidade (que vai de 1 a 100), será necessário um algoritmo para encontrar a qualidade exata que resulte no tamanho desejado em KB ou MB.
1. **Implementar uma Busca Binária:** 
   * O programa salva a imagem temporariamente com qualidade 50 e verifica o tamanho do arquivo gerado.
   * Se o tamanho ficou maior que o limite definido pelo usuário, o programa testa a qualidade 25. Se ficou menor, testa 75. 
   * O processo se repete dividindo os intervalos pela metade até encontrar a qualidade que mais se aproxime do limite estabelecido, garantindo a melhor resolução possível dentro daquela restrição.
2. **Tratamento de Formatos:** Formatos como PNG utilizam compressão sem perdas (lossless). Para garantir a redução drástica de tamanho exigida, o código precisará converter essas imagens para JPEG antes de aplicar a compressão.

## Fase 3: Interface do Usuário (UI)
Criar uma interface gráfica tornará o software mais profissional e alinhado com a proposta de uma aplicação prática para o usuário final.
1. **Ferramenta Nativa:** Utilizar a biblioteca `Tkinter`, que já vem instalada por padrão com o Python e não exige instalações complexas de terceiros.
2. **Elementos da Interface:** Criar uma janela simples contendo:
   * Um botão para o usuário procurar e selecionar a imagem de entrada em seu computador.
   * Um campo de texto para o usuário inserir o tamanho máximo desejado para o novo arquivo.
   * Um botão de ação "Comprimir".

## Fase 4: Como criar o Executável (O Passo Crítico)
Transformar o código em um executável em Python é um processo direto usando a ferramenta `PyInstaller`. Ela empacota o código, as dependências (como o Pillow) e o interpretador Python em um único arquivo.
1. Quando o código estiver totalmente pronto e funcionando, abra o terminal do computador.
2. Instale a ferramenta executando o comando: `pip install pyinstaller`
3. No terminal, navegue até a pasta onde está o arquivo principal de código (por exemplo, `main.py`).
4. Execute o seguinte comando:
   ```bash
   pyinstaller --onefile --windowed main.py
   ```
   * O parâmetro `--onefile` garante que tudo seja compactado em um único arquivo executável (`.exe`).
   * O parâmetro `--windowed` (ou `--noconsole`) oculta a janela preta do terminal quando o usuário abre o programa, mostrando apenas a interface gráfica.
5. Após a conclusão, será criada uma pasta chamada `dist` no diretório. Lá dentro estará o executável pronto para ser entregue e executado em qualquer computador, sem necessidade de instalar o Python.

## Fase 5: Testes e Documentação
1. **Execução de Testes:** Realizar testes práticos com várias imagens de entrada diferentes, validando se o tamanho limite nunca é ultrapassado.
2. **Coleta de Dados:** Documentar a relação entre o tamanho final atingido e a qualidade da imagem resultante (avaliando se a imagem ficou muito borrada ou pixelada em taxas de compressão altas).
3. **Entrega Final:** Adicionar ao repositório o código-fonte final, os arquivos de compilação (como o `requirements.txt`) e a versão executável pronta do software.