def identifica_numero_par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

def main():
    try:
        # Solicitar ao usuário para digitar um número
        numero = int(input("Digite um número inteiro: "))

        #  verificar se o número é par ou ímpar
        resultado = identifica_numero_par_ou_impar(numero)
        print(f"O número {numero} é {resultado}.")

    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
