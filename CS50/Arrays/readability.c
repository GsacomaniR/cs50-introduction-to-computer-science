#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(char text[]);
int count_words(char text[]);
int count_sentences(char text[]);

int main(void)
{
    // Solicitar texto do usuário
    char text[10000];
    printf("Texto: ");
    fgets(text, sizeof(text), stdin);
    
    // Remover o caractere de nova linha se presente
    text[strcspn(text, "\n")] = 0;
    
    // Contar letras, palavras e frases
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    
    // Calcular médias por 100 palavras
    float L = (letters / (float)words) * 100;
    float S = (sentences / (float)words) * 100;
    
    // Calcular índice Coleman-Liau
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int grade = round(index);
    
    // Exibir resultado
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", grade);
    }
    
    return 0;
}

int count_letters(char text[])
{
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (isalpha(text[i])) // Verifica se é uma letra (A-Z ou a-z)
        {
            count++;
        }
    }
    return count;
}

int count_words(char text[])
{
    int count = 0;
    int in_word = 0; // Flag para saber se estamos dentro de uma palavra
    
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (isspace(text[i])) // Se é espaço, tabulação, nova linha, etc.
        {
            if (in_word)
            {
                count++;
                in_word = 0;
            }
        }
        else
        {
            in_word = 1;
        }
    }
    
    // Contar a última palavra se o texto não terminar com espaço
    if (in_word)
    {
        count++;
    }
    
    return count;
}

int count_sentences(char text[])
{
    int count = 0;
    
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count++;
        }
    }
    
    return count;
}
