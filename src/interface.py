import tkinter as tk
from tkinter import filedialog, messagebox
import os

class AppCompressor:
    def __init__(self, root, funcao_compressao):
        self.root = root
        self.funcao_compressao = funcao_compressao
        self.root.title("Compressor de Imagens")
        self.root.geometry("400x250")
        
        self.caminho_imagem_entrada = None

        # Título
        self.label_titulo = tk.Label(root, text="Otimizador de Imagens", font=("Arial", 14, "bold"))
        self.label_titulo.pack(pady=10)

        # Botão para selecionar a imagem
        self.btn_selecionar = tk.Button(root, text="1. Selecionar Imagem", command=self.selecionar_imagem)
        self.btn_selecionar.pack(pady=5)

        # Rótulo que mostra o nome do arquivo selecionado
        self.label_arquivo = tk.Label(root, text="Nenhuma imagem selecionada", fg="gray")
        self.label_arquivo.pack(pady=5)

        # Campo de texto para o tamanho desejado
        self.label_tamanho = tk.Label(root, text="2. Tamanho máximo desejado (em KB):")
        self.label_tamanho.pack(pady=5)
        
        self.entry_tamanho = tk.Entry(root, width=15, justify="center")
        self.entry_tamanho.pack(pady=5)

        # Botão final para comprimir
        self.btn_comprimir = tk.Button(root, text="3. Comprimir Imagem", command=self.executar_compressao, bg="#4CAF50", fg="white")
        self.btn_comprimir.pack(pady=15)

    def selecionar_imagem(self):
        caminho = filedialog.askopenfilename(
            title="Selecione a imagem original",
            filetypes=[("Arquivos de Imagem", "*.png *.jpg *.jpeg *.bmp")]
        )
        if caminho:
            self.caminho_imagem_entrada = caminho
            nome_arquivo = os.path.basename(caminho)
            self.label_arquivo.config(text=f"Selecionado: {nome_arquivo}", fg="black")

    def executar_compressao(self):
        if not self.caminho_imagem_entrada:
            messagebox.showwarning("Atenção", "Por favor, selecione uma imagem primeiro.")
            return
            
        tamanho_digitado = self.entry_tamanho.get()
        if not tamanho_digitado.isdigit() or int(tamanho_digitado) <= 0:
            messagebox.showerror("Erro", "Por favor, digite um valor numérico válido (maior que 0) para o tamanho em KB.")
            return

        tamanho_alvo_kb = int(tamanho_digitado)
        
        diretorio_origem = os.path.dirname(self.caminho_imagem_entrada)
        nome_original = os.path.basename(self.caminho_imagem_entrada)
        nome_sem_extensao = os.path.splitext(nome_original)[0]
        caminho_saida = os.path.join(diretorio_origem, f"{nome_sem_extensao}_comprimida.jpg")

        # Recebe o status (True/False) e a mensagem gerada pela lógica
        sucesso, mensagem = self.funcao_compressao(self.caminho_imagem_entrada, caminho_saida, tamanho_alvo_kb)

        # Exibe o pop-up correto baseado no resultado
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
        else:
            messagebox.showwarning("Aviso de Limite", mensagem)