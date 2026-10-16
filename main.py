import tkinter as tk
from src.interface import AppCompressor
from src.compressor import comprimir_imagem_para_tamanho

def main():
    # Cria a janela base do sistema operacional
    janela_principal = tk.Tk()
    
    # Inicia a nossa aplicação passando a janela e a função de compressão
    app = AppCompressor(janela_principal, comprimir_imagem_para_tamanho)
    
    # Mantém a janela aberta e rodando
    janela_principal.mainloop()

if __name__ == "__main__":
    main()