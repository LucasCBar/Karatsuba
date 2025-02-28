# Karatsuba

## Descrição do Projeto
Este código apresenta o algoritmo de Karatsuba em Python, empregada para multiplicação ágil e eficiente de números inteiros grandes. Esse método reduz a complexidade computacional da multiplicação tradicional, proporcionando um desempenho mais rápido e eficaz.

## Como executar o projeto

### Requisitos
- Python 3.13 instalado

### Passo a passo
1. Clone este repositório:
   ```bash
   git clone https://github.com/LucasCBar/Karatsuba.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd Algoritmo-de-Karatsuba-python
   ```
3. Execute o script principal:
   ```bash
   python main.py
   ```
4. Digite dois números inteiros quando solicitado e visualize o resultado da multiplicação.

## Implementação do Algoritmo de Karatsuba

```python
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
```

## Análise da Complexidade do Algoritmo

### Complexidade Assintótica
- Melhor Caso: O(n^log_2(3)) ≈ O(n^1.58)
- Caso Médio: O(n^log_2(3)) ≈ O(n^1.58)
- Pior Caso: O(n^log_2(3)) ≈ O(n^1.58)

### Complexidade Ciclomática
A complexidade ciclomática pode ser calculada através do grafo de fluxo de controle do algoritmo:

- Número de arestas (E): 6
- Número de nós (N): 5
- Número de componentes conexos (P): 1

**Complexidade Ciclomática (M) = E - N + 2P = 6 - 5 + 2(1) = 3**

