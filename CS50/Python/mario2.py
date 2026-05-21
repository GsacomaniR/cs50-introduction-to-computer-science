from cs50 import get_int

def main():
    # Solicita a altura ao usuário
    while True:
        height = get_int("Height: ")
        if height >= 1 and height <= 8:
            break
    
    # Gera as pirâmides
    for i in range(1, height + 1):
        # Primeira pirâmide (esquerda)
        spaces_left = height - i
        print(" " * spaces_left, end="")
        print("#" * i, end="")
        
        # Espaço entre as pirâmides
        print("  ", end="")
        
        # Segunda pirâmide (direita)
        print("#" * i)

if __name__ == "__main__":
    main()
