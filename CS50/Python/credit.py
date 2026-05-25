from cs50 import get_string

def main():
    # Obter o número do cartão do usuário
    number = get_string("Number: ")
    
    # Verificar se a entrada contém apenas dígitos
    if not number.isdigit():
        print("INVALID")
        return
    
    # Verificar se o comprimento é válido
    length = len(number)
    if length not in [13, 15, 16]:
        print("INVALID")
        return
    
    # Validar usando o algoritmo de Luhn
    if not luhn_algorithm(number):
        print("INVALID")
        return
    
    # Identificar a bandeira do cartão
    card_type = identify_card(number, length)
    print(card_type)

def luhn_algorithm(number):
    """
    Implementa o algoritmo de Luhn para validar o número do cartão
    Retorna True se válido, False caso contrário
    """
    total = 0
    # Percorrer os dígitos da direita para a esquerda
    for i, digit_char in enumerate(reversed(number)):
        digit = int(digit_char)
        
        # Posições ímpares (começando em 1) - dígitos que serão dobrados
        if i % 2 == 1:
            doubled = digit * 2
            # Somar os dígitos do resultado
            total += (doubled // 10) + (doubled % 10)
        else:
            # Posições pares - somar diretamente
            total += digit
    
    # Válido se o total for divisível por 10
    return total % 10 == 0

def identify_card(number, length):
    """
    Identifica a bandeira do cartão baseado nos primeiros dígitos e comprimento
    Retorna AMEX, MASTERCARD, VISA ou INVALID
    """
    # Obter os primeiros dígitos como inteiros
    first_digit = int(number[0])
    first_two_digits = int(number[:2])
    
    # Verificar AMEX (15 dígitos, começa com 34 ou 37)
    if length == 15 and first_two_digits in [34, 37]:
        return "AMEX"
    
    # Verificar MASTERCARD (16 dígitos, começa com 51, 52, 53, 54 ou 55)
    if length == 16 and 51 <= first_two_digits <= 55:
        return "MASTERCARD"
    
    # Verificar VISA (13 ou 16 dígitos, começa com 4)
    if (length == 13 or length == 16) and first_digit == 4:
        return "VISA"
    
    return "INVALID"

if __name__ == "__main__":
    main()
