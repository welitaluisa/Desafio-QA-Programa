# A função range() tem três parâmetros principais:
# start (início): O valor inicial da sequência (opcional, padrão é 0).
# stop (parada): O valor até o qual a sequência será gerada (não incluído).
# step (passo): O intervalo entre os números na sequência (opcional, padrão é 1).

import random

def gerar_numeros_mega_sena():
    # Gera 6 números aleatórios entre 1 e 60, sem repetições
    # A função random.sample() garante que os elementos selecionados sejam únicos na amostra resultante.
    numeros_mega_sena = random.sample(range(1, 61), 6)
    return numeros_mega_sena

def main():
    # Gera e exibe a lista de números para a Mega Sena
    numeros_mega_sena = gerar_numeros_mega_sena()
    print("Números da Mega Sena:")
    for numero in numeros_mega_sena:
        print(numero)

if __name__ == "__main__":
    main()
