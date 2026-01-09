#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int altura;

    do
    {
        altura = get_int("Altura: ");
    }
    while (altura < 1 || altura > 8);

    for (int linha = 1; linha <= altura; linha++)
    {
        // imprime espaços
        for (int espaco = 0; espaco < altura - linha; espaco++)
        {
            printf(" ");
        }

        // imprime #
        for (int hash = 0; hash < linha; hash++)
        {
            printf("#");
        }

        // pula linha
            printf("  ");
            for (int hash = 0; hash < linha; hash++)
        {
            printf("#");
        }
        printf("\n");
    }
}
