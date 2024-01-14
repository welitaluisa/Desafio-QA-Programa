# Programa separa o texto digitado em palavras individual e retorna quantas palavras foram encontradas
def contar_palavras(texto):
    palavras = texto.split()  # split() divide o texto em palavras separadas por espaços em branco.
    num_palavras = len(palavras) # conta numero de palavras encontradas 
    
    if num_palavras == 1:
        return "O texto contém uma palavra."
    else:
        return f"O texto contém {num_palavras} palavras."  # Retorna o número de palavras


# Solicita a entrada do usuário
texto_usuario = input("Digite uma palavra ou frase: ")
resultado_contagem = contar_palavras(texto_usuario)
print(f"{resultado_contagem}")
