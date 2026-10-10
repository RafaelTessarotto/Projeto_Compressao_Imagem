import io
import os
from PIL import Image

def comprimir_imagem_para_tamanho(caminho_entrada, caminho_saida, tamanho_maximo_kb):
    """
    Comprime uma imagem para que o ficheiro resultante tenha um tamanho menor ou igual 
    ao especificado, mantendo a maior qualidade possível através de busca binária.
    """
    # Converter o tamanho desejado de Kilobytes para Bytes
    tamanho_maximo_bytes = tamanho_maximo_kb * 1024
    
    try:
        imagem = Image.open(caminho_entrada)
        
        # O formato JPEG não suporta canais alfa (transparência).
        # Se a imagem for PNG (RGBA) ou possuir paleta (P), é necessário convertê-la para RGB.
        if imagem.mode in ("RGBA", "P", "LA"):
            imagem = imagem.convert("RGB")
            
    except Exception as e:
        print(f"Erro ao processar a imagem de entrada: {e}")
        return False

    # Variáveis para a busca binária da qualidade (1 a 100)
    limite_inferior = 1
    limite_superior = 100
    melhor_qualidade = 1
    
    # Processo de busca binária utilizando buffer em memória
    while limite_inferior <= limite_superior:
        qualidade_teste = (limite_inferior + limite_superior) // 2
        
        # Utilizar BytesIO para testar o tamanho do ficheiro sem escrever no disco
        buffer_memoria = io.BytesIO()
        imagem.save(buffer_memoria, format="JPEG", quality=qualidade_teste)
        tamanho_teste = buffer_memoria.tell()
        
        # Avaliar o resultado
        if tamanho_teste <= tamanho_maximo_bytes:
            # O tamanho está dentro do limite. Guardamos esta qualidade como a melhor até agora.
            melhor_qualidade = qualidade_teste
            # Tentamos uma qualidade maior (metade superior) para ver se ainda cabe no limite
            limite_inferior = qualidade_teste + 1
        else:
            # O tamanho excedeu o limite. Precisamos de uma qualidade menor (metade inferior)
            limite_superior = qualidade_teste - 1

    # Após encontrar a qualidade ideal, escrevemos o ficheiro final no disco
    try:
        imagem.save(caminho_saida, format="JPEG", quality=melhor_qualidade)
        
        tamanho_original_kb = os.path.getsize(caminho_entrada) / 1024
        tamanho_final_kb = os.path.getsize(caminho_saida) / 1024
        
        print("\n--- Resultado da Compressão ---")
        print(f"Tamanho Original: {tamanho_original_kb:.2f} KB")
        print(f"Tamanho Final: {tamanho_final_kb:.2f} KB (Alvo: {tamanho_maximo_kb} KB)")
        print(f"Qualidade JPEG utilizada: {melhor_qualidade}/100")
        
        # Caso extremo: mesmo na qualidade 1, o ficheiro ficou maior que o limite
        if tamanho_final_kb > tamanho_maximo_kb:
            print("Aviso: O limite estipulado é demasiado rigoroso. Mesmo com a qualidade mínima, não foi possível atingir o tamanho desejado sem redimensionar a imagem.")
            
        return True
        
    except Exception as e:
        print(f"Erro ao guardar a imagem final: {e}")
        return False

# Bloco para testar o algoritmo de forma isolada
if __name__ == "__main__":
    # Exemplo de utilização (substituam 'teste.png' por uma imagem real no vosso computador)
    imagem_teste = "teste.png" 
    imagem_resultado = "resultado.jpg"
    tamanho_alvo = 500 # 500 KB
    
    if os.path.exists(imagem_teste):
        comprimir_imagem_para_tamanho(imagem_teste, imagem_resultado, tamanho_alvo)
    else:
        print(f"Coloquem uma imagem chamada '{imagem_teste}' na pasta para testar o script.")