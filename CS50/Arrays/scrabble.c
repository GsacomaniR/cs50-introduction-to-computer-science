#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Valores de pontos para cada letra do alfabeto (A-Z)
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

// Protótipo da função
int compute_score(string word);

int main(void)
{
    // Solicitar ao usuário duas palavras
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Calcular os pontos de cada palavra
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Imprimir o vencedor
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    int score = 0;

    // Percorrer cada caractere da palavra
    for (int i = 0, length = strlen(word); i < length; i++)
    {
        char c = word[i];

        // Verificar se é uma letra maiúscula
        if (isupper(c))
        {
            // Converter 'A' (65) para índice 0, 'B' (66) para índice 1, etc.
            score += POINTS[c - 'A'];
        }
        // Verificar se é uma letra minúscula
        else if (islower(c))
        {
            // Converter 'a' (97) para índice 0, 'b' (98) para índice 1, etc.
            score += POINTS[c - 'a'];
        }
        // Se não for uma letra, não adiciona pontos (já vale 0)
    }

    return score;
}
