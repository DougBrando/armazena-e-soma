def obter_numero():
    """Função para obter um número inteiro do usuário com tratamento de exceção."""
    while True:
        try:
            return int(input('Digite um número (ou 999 para encerrar): '))  # Solicita um número ao usuário
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")  # Mensagem de erro para entradas inválidas

def main():
    """Função principal que executa o programa de soma de números."""
    c = s = 0  # Inicializa o contador de números e a soma

    while True:  # Inicia um loop infinito
        n = obter_numero()  # Obtém um número do usuário

        if n == 999:  # Verifica se o número digitado é 999
            break  # Encerra o loop se o número for 999

        s += n  # Adiciona o número digitado à soma total
        c += 1  # Incrementa o contador de números digitados

    # Exibe o total de números digitados e a soma
    print(f'Você digitou {c} número(s) e sua soma é de {s}')

if __name__ == "__main__":
    main()  # Executa a função principal
