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
        return False, f"Erro ao processar a imagem de entrada: {e}"

    # TESTE DE LIMITE MÍNIMO: Verifica se é fisicamente possível atingir o alvo
    buffer_min = io.BytesIO()
    imagem.save(buffer_min, format="JPEG", quality=1)
    tamanho_min_bytes = buffer_min.tell()
    tamanho_min_kb = tamanho_min_bytes / 1024

    # Se a qualidade mínima ainda for maior que o alvo, aborta e avisa o limite
    if tamanho_min_bytes > tamanho_maximo_bytes:
        msg_erro = (f"O limite de {tamanho_maximo_kb} KB é muito rigoroso para esta resolução.\n\n"
                    f"O tamanho mínimo possível para esta imagem é {tamanho_min_kb:.2f} KB.")
        return False, msg_erro

    # Se for possível, inicia a busca binária
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
        tamanho_final_kb = os.path.getsize(caminho_saida) / 1024
        nome_saida = os.path.basename(caminho_saida)
        
        msg_sucesso = (f"Imagem comprimida com sucesso!\n\n"
                       f"Salva como: {nome_saida}\n"
                       f"Tamanho Final: {tamanho_final_kb:.2f} KB\n"
                       f"Qualidade utilizada: {melhor_qualidade}/100")
        return True, msg_sucesso
        
    except Exception as e:
        return False, f"Erro ao salvar a imagem final: {e}"