"""
Implementação do algoritmo de Karatsuba para multiplicação eficiente de dois números inteiros.

:param x: Primeiro número inteiro
:param y: Segundo número inteiro
:return: Resultado da multiplicação de x por y
"""
import math

def multiplicacao_karatsuba(a: int, b: int) -> int:
    if a < 10 or b < 10:
        return a * b
    
    tam = max(len(str(a)), len(str(b)))
    meio = math.ceil(tam / 2)
    
    parte_alta_a, parte_baixa_a = divmod(a, 10 ** meio)
    parte_alta_b, parte_baixa_b = divmod(b, 10 ** meio)
    
    produto1 = multiplicacao_karatsuba(parte_baixa_a, parte_baixa_b)
    produto2 = multiplicacao_karatsuba(parte_alta_a, parte_alta_b)
    produto3 = multiplicacao_karatsuba((parte_baixa_a + parte_alta_a), (parte_baixa_b + parte_alta_b))
    
    return (produto2 * 10 ** (2 * meio)) + ((produto3 - produto2 - produto1) * 10 ** meio) + produto1

if __name__ == "__main__":
    valor1 = int(input("Informe o primeiro valor: "))
    valor2 = int(input("Informe o segundo valor: "))
    resultado = multiplicacao_karatsuba(valor1, valor2)
    print(f"O resultado da multiplicação é: {resultado}")
