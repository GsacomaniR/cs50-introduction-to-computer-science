from cs50 import get_int

def main():
    # Solicita a altura ao usuário
    while True:
        height = get_int("Height: ")
        if height >= 1 and height <= 8:
            break
    
    # Constrói a pirâmide
    for i in range(1, height + 1):
        # Calcula o número de espaços e hashes
        spaces = height - i
        hashes = i
        
        # Imprime a linha
        print(" " * spaces + "#" * hashes)

if __name__ == "__main__":
    main()
