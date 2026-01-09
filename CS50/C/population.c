#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start;
    do
    {
        start = get_int("Start size: ");
    }
    while (start < 9);

    int end;
    do
    {
        end = get_int("End size: ");
    }
    while (end < start);

    int years = 0;
    int population = start;

    while (population < end)
    {
        population = population + (population / 3) - (population / 4);
        years++;
    }

    printf("Years: %i\n", years);
}
