# Inicializa as variáveis
n = c = s = 0  # n: número digitado, c: contador de números, s: soma dos números

while True:  # Inicia um loop infinito
    n = int(input('Digite um número: '))  # Solicita ao usuário que digite um número
    s += n  # Adiciona o número digitado à soma total
    c += 1  # Incrementa o contador de números digitados

    # Verifica se o número digitado é 999
    if n == 999:
        break  # Encerra o loop se o número for 999

# Exibe o total de números digitados e a soma
print(f'Você digitou {c} número(s) e sua soma é de {s}')
