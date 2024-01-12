
class Calculadora:
    @staticmethod
    def somar_dois_numeros(num1, num2):
        return num1 + num2

    @staticmethod
    def subtrair_dois_numeros(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplicar_dois_numeros(num1, num2):
        return num1 * num2

    @staticmethod
    def dividir_dois_numeros(num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("Não é possível dividir por zero")
            return 0

if __name__ == "__main__":
    # chamar as 4 operações
    print("1 + 5 =", Calculadora.somar_dois_numeros(1, 5))
    print("5 - 1 =", Calculadora.subtrair_dois_numeros(5, 1))
    print("2 * 30 =", Calculadora.multiplicar_dois_numeros(2, 30))
    print("21 / 7 =", Calculadora.dividir_dois_numeros(21, 7))
    print("10 / 0 =", Calculadora.dividir_dois_numeros(10, 0))
    print("1 + -5 =", Calculadora.somar_dois_numeros(1, -5)) 
    print("2 *cls -30 =", Calculadora.multiplicar_dois_numeros(2, -30))
    print("(-21) / 7 =", Calculadora.dividir_dois_numeros(-21, 7))  
    print("-10 / 0 =", Calculadora.dividir_dois_numeros(-10, 0))

