import io
import os
from PIL import Image

def comprimir_imagem_para_tamanho(caminho_entrada, caminho_saida, tamanho_maximo_kb):
    tamanho_maximo_bytes = tamanho_maximo_kb * 1024
    
    try:
        imagem = Image.open(caminho_entrada)
        if imagem.mode in ("RGBA", "P", "LA"):
            imagem = imagem.convert("RGB")
    except Exception as e:
        print(f"Erro ao processar a imagem de entrada: {e}")
        return False

    limite_inferior = 1
    limite_superior = 100
    melhor_qualidade = 1
    
    while limite_inferior <= limite_superior:
        qualidade_teste = (limite_inferior + limite_superior) // 2
        
        buffer_memoria = io.BytesIO()
        imagem.save(buffer_memoria, format="JPEG", quality=qualidade_teste)
        tamanho_teste = buffer_memoria.tell()
        
        if tamanho_teste <= tamanho_maximo_bytes:
            melhor_qualidade = qualidade_teste
            limite_inferior = qualidade_teste + 1
        else:
            limite_superior = qualidade_teste - 1

    try:
        imagem.save(caminho_saida, format="JPEG", quality=melhor_qualidade)
        
        tamanho_original_kb = os.path.getsize(caminho_entrada) / 1024
        tamanho_final_kb = os.path.getsize(caminho_saida) / 1024
        
        print("\n--- Resultado da Compressão ---")
        print(f"Tamanho Original: {tamanho_original_kb:.2f} KB")
        print(f"Tamanho Final: {tamanho_final_kb:.2f} KB (Alvo: {tamanho_maximo_kb} KB)")
        print(f"Qualidade JPEG utilizada: {melhor_qualidade}/100")
        
        if tamanho_final_kb > tamanho_maximo_kb:
            print("Aviso: O limite estipulado é muito rigoroso para as dimensões da imagem.")
            
        return True
        
    except Exception as e:
        print(f"Erro ao salvar a imagem final: {e}")
        return False

if __name__ == "__main__":
    # Variáveis de teste
    imagem_teste = "teste.png" 
    imagem_resultado = "resultado.png"
    tamanho_alvo = 500 # Tamanho máximo desejado em KB
    
    if os.path.exists(imagem_teste):
        comprimir_imagem_para_tamanho(imagem_teste, imagem_resultado, tamanho_alvo)
    else:
        print(f"Erro: Coloque uma imagem chamada '{imagem_teste}' na mesma pasta onde está executando o script.")