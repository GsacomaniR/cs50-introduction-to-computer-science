#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    // Verifica se o programa foi executado com exatamente um argumento
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Verifica se todos os caracteres do argumento são dígitos
    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    // Converte o argumento de string para inteiro
    int key = atoi(argv[1]);

    // Solicita o texto simples ao usuário
    char plaintext[1000];
    printf("plaintext: ");
    fgets(plaintext, sizeof(plaintext), stdin);

    // Remove o caractere de nova linha se existir
    size_t len = strlen(plaintext);
    if (len > 0 && plaintext[len - 1] == '\n')
    {
        plaintext[len - 1] = '\0';
    }

    printf("ciphertext: ");

    // Processa cada caractere do texto simples
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char c = plaintext[i];

        if (isupper(c))
        {
            // Para letras maiúsculas: A=0, B=1, ..., Z=25
            // (c - 'A' + key) % 26 dá a nova posição no alfabeto
            // + 'A' converte de volta para ASCII
            printf("%c", ((c - 'A' + key) % 26) + 'A');
        }
        else if (islower(c))
        {
            // Para letras minúsculas: a=0, b=1, ..., z=25
            printf("%c", ((c - 'a' + key) % 26) + 'a');
        }
        else
        {
            // Mantém caracteres não alfabéticos inalterados
            printf("%c", c);
        }
    }

    printf("\n");
    return 0;
}
