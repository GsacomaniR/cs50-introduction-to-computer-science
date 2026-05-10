#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

typedef uint8_t BYTE;

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // Verifica se o número de argumentos está correto
    if (argc != 2)
    {
        printf("Uso: ./recover imagem\n");
        return 1;
    }

    // Abre o arquivo da imagem forense
    FILE *input_file = fopen(argv[1], "r");
    if (input_file == NULL)
    {
        printf("Erro: Não foi possível abrir o arquivo %s\n", argv[1]);
        return 1;
    }

    BYTE buffer[BLOCK_SIZE];
    int file_count = 0;
    FILE *output_file = NULL;
    char filename[8]; // Nome do arquivo: ###.jpg (7 caracteres + \0)
    bool found_jpeg = false;

    // Lê o arquivo em blocos de 512 bytes
    while (fread(buffer, sizeof(BYTE), BLOCK_SIZE, input_file) == BLOCK_SIZE)
    {
        // Verifica se é o início de um JPEG
        // Os primeiros 4 bytes de um JPEG são: 0xff, 0xd8, 0xff, 0xe? (e0, e1, etc.)
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            // Se já estava escrevendo um arquivo, fecha o anterior
            if (output_file != NULL)
            {
                fclose(output_file);
                output_file = NULL;
            }

            // Cria um novo arquivo JPEG
            sprintf(filename, "%03d.jpg", file_count);
            output_file = fopen(filename, "w");

            if (output_file == NULL)
            {
                printf("Erro: Não foi possível criar o arquivo %s\n", filename);
                fclose(input_file);
                return 1;
            }

            file_count++;
            found_jpeg = true;

            // Escreve o bloco atual no novo arquivo
            fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, output_file);
        }
        else if (found_jpeg && output_file != NULL)
        {
            // Está no meio de um JPEG, continua escrevendo no arquivo atual
            fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, output_file);
        }
    }

    // Fecha o último arquivo, se houver
    if (output_file != NULL)
    {
        fclose(output_file);
    }

    // Fecha o arquivo de entrada
    fclose(input_file);

    // Verifica se encontrou pelo menos um JPEG
    if (file_count == 0)
    {
        printf("Nenhum JPEG encontrado no arquivo.\n");
        return 1;
    }

    printf("Recuperados %d JPEGs com sucesso.\n", file_count);
    return 0;
}
