#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long numero = get_long("Número: ");

    long temp = numero;
    int soma = 0;
    int posicao = 0;
    int digitos = 0;

    // Algoritmo de Luhn
    while (temp > 0)
    {
        int digito = temp % 10;

        if (posicao % 2 == 1)
        {
            digito *= 2;

            if (digito > 9)
            {
                digito = (digito / 10) + (digito % 10);
            }
        }

        soma += digito;
        temp /= 10;
        posicao++;
        digitos++;
    }

    // Se não passar no Luhn
    if (soma % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    // Descobrir os primeiros dígitos
    temp = numero;
    while (temp >= 100)
    {
        temp /= 10;
    }

    int primeiros = temp;

    // Verificar bandeira
    if ((primeiros == 34 || primeiros == 37) && digitos == 15)
    {
        printf("AMEX\n");
    }
    else if (primeiros >= 51 && primeiros <= 55 && digitos == 16)
    {
        printf("MASTERCARD\n");
    }
    else if ((primeiros / 10 == 4) && (digitos == 13 || digitos == 16))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
