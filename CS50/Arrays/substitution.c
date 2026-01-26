#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

// Função para verificar se a chave é válida
bool validar_chave(char *chave) {
    int tamanho = strlen(chave);

    // Verifica se a chave tem 26 caracteres
    if (tamanho != 26) {
        printf("A chave deve conter 26 caracteres.\n");
        return false;
    }

    // Array para verificar letras repetidas
    int letras[26] = {0};

    for (int i = 0; i < tamanho; i++) {
        // Verifica se o caractere é alfabético
        if (!isalpha(chave[i])) {
            printf("A chave deve conter apenas caracteres alfabéticos.\n");
            return false;
        }

        // Converte para maiúscula para verificação
        char maiuscula = toupper(chave[i]);

        // Verifica se esta letra já apareceu
        if (letras[maiuscula - 'A'] == 1) {
            printf("A chave não pode conter letras repetidas.\n");
            return false;
        }

        // Marca a letra como encontrada
        letras[maiuscula - 'A'] = 1;
    }

    // Verifica se todas as letras foram encontradas
    for (int i = 0; i < 26; i++) {
        if (letras[i] == 0) {
            printf("A chave deve conter todas as 26 letras do alfabeto.\n");
            return false;
        }
    }

    return true;
}

// Função para criptografar um caractere usando a chave
char criptografar_caractere(char c, char *chave) {
    if (isupper(c)) {
        // Para letras maiúsculas
        int indice = c - 'A';
        return toupper(chave[indice]);
    } else if (islower(c)) {
        // Para letras minúsculas
        int indice = c - 'a';
        return tolower(chave[indice]);
    } else {
        // Para caracteres não alfabéticos
        return c;
    }
}

int main(int argc, char *argv[]) {
    // Verifica se foi fornecido exatamente um argumento de linha de comando
    if (argc != 2) {
        printf("Uso: ./substitution chave_de_substituicao\n");
        return 1;
    }

    // Converte a chave para maiúsculas para processamento interno
    char chave[27];
    for (int i = 0; i < 26; i++) {
        chave[i] = toupper(argv[1][i]);
    }
    chave[26] = '\0'; // Terminador de string

    // Valida a chave
    if (!validar_chave(chave)) {
        return 1;
    }

    // Solicita o texto simples
    printf("texto simples: ");

    // Lê a entrada do usuário
    char texto[1000];
    fgets(texto, sizeof(texto), stdin);

    // Remove o caractere de nova linha do final, se existir
    texto[strcspn(texto, "\n")] = '\0';

    // Criptografa o texto
    printf("texto cifrado: ");

    for (int i = 0; texto[i] != '\0'; i++) {
        printf("%c", criptografar_caractere(texto[i], chave));
    }

    printf("\n");
    return 0;
}
