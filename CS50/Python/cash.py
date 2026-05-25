from cs50 import get_float

def main():
    # Solicitar ao usuário o valor do troco devido
    while True:
        change = get_float("Change owed: ")
        if change >= 0:
            break
    
    # Converter para centavos para evitar problemas de ponto flutuante
    cents = round(change * 100)
    
    # Contador de moedas
    coins = 0
    
    # Moedas disponíveis: 25¢, 10¢, 5¢, 1¢
    while cents >= 25:
        cents -= 25
        coins += 1
    
    while cents >= 10:
        cents -= 10
        coins += 1
    
    while cents >= 5:
        cents -= 5
        coins += 1
    
    while cents >= 1:
        cents -= 1
        coins += 1
    
    # Imprimir o resultado
    print(coins)

if __name__ == "__main__":
    main()
