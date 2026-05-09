#include "helpers.h"
#include <math.h>

// Converte imagem para escala de cinza
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Calcula a média dos valores RGB
            int media = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);

            // Define todos os canais para o valor da média
            image[i][j].rgbtBlue = media;
            image[i][j].rgbtGreen = media;
            image[i][j].rgbtRed = media;
        }
    }
}

// Reflete a imagem horizontalmente
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // Troca o pixel da posição j com o pixel da posição (width - 1 - j)
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
}

// Aplica efeito blur (desfoque)
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Cria uma cópia da imagem original
    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // Aplica o blur em cada pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int totalRed = 0, totalGreen = 0, totalBlue = 0;
            int count = 0;

            // Percorre os 3x3 vizinhos (incluindo o próprio pixel)
            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    // Verifica se o vizinho está dentro dos limites da imagem
                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        totalRed += copy[ni][nj].rgbtRed;
                        totalGreen += copy[ni][nj].rgbtGreen;
                        totalBlue += copy[ni][nj].rgbtBlue;
                        count++;
                    }
                }
            }

            // Calcula a média e atualiza o pixel
            image[i][j].rgbtRed = round((float)totalRed / count);
            image[i][j].rgbtGreen = round((float)totalGreen / count);
            image[i][j].rgbtBlue = round((float)totalBlue / count);
        }
    }
}

// Detecta bordas usando o algoritmo de Sobel
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Cria uma cópia da imagem original
    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // Kernels de Sobel para Gx e Gy
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    // Aplica a detecção de bordas em cada pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Variáveis para acumular os valores de Gx e Gy para cada canal
            int Gx_red = 0, Gx_green = 0, Gx_blue = 0;
            int Gy_red = 0, Gy_green = 0, Gy_blue = 0;

            // Percorre os 3x3 vizinhos
            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    // Se estiver fora dos limites, considera como preto (0)
                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        Gx_red += copy[ni][nj].rgbtRed * Gx[di + 1][dj + 1];
                        Gx_green += copy[ni][nj].rgbtGreen * Gx[di + 1][dj + 1];
                        Gx_blue += copy[ni][nj].rgbtBlue * Gx[di + 1][dj + 1];

                        Gy_red += copy[ni][nj].rgbtRed * Gy[di + 1][dj + 1];
                        Gy_green += copy[ni][nj].rgbtGreen * Gy[di + 1][dj + 1];
                        Gy_blue += copy[ni][nj].rgbtBlue * Gy[di + 1][dj + 1];
                    }
                }
            }

            // Calcula a magnitude do gradiente (sqrt(Gx^2 + Gy^2))
            int sobel_red = round(sqrt(Gx_red * Gx_red + Gy_red * Gy_red));
            int sobel_green = round(sqrt(Gx_green * Gx_green + Gy_green * Gy_green));
            int sobel_blue = round(sqrt(Gx_blue * Gx_blue + Gy_blue * Gy_blue));

            // Garante que os valores não ultrapassem 255
            image[i][j].rgbtRed = (sobel_red > 255) ? 255 : sobel_red;
            image[i][j].rgbtGreen = (sobel_green > 255) ? 255 : sobel_green;
            image[i][j].rgbtBlue = (sobel_blue > 255) ? 255 : sobel_blue;
        }
    }
}
