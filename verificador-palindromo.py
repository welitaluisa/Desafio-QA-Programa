# esse programa verifica se a palavra ou frase digitada é palindromo
# Um palíndromo é uma palavra, frase, número ou qualquer outra sequência de caracteres que permanece igual quando lida de trás para frente 

def eh_palindromo(frase):
    # Remove espaços, vírgulas, pontos, ponto de exclamação, ponto de interrogação e converte para a string para minúsculas
    frase_formatada =  frase.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").lower()
    
    # Verificar se a frase é igual à sua reversa
    return frase_formatada == frase_formatada[::-1]

# Solicitar entrada do usuário
entrada = input("Digite uma frase ou palavra: ")

# Verificar se é um palíndromo e exibir o resultado
if eh_palindromo(entrada):
    print(f"'{entrada}' é um palíndromo!")
else:
    print(f"'{entrada}' não é um palíndromo.")