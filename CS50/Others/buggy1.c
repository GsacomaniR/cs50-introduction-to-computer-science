#include <cs50.h>
#include <stdio.h>

//  Prototype
int get_negative_int(void);

int main(void)
{
    // Get negative integer from use
    int i = get_negative_int();
    printf("%i\n", i);
}

int get_negative_int(void)
{
    int n;
    do
    {
        n = get_int("Negative_Integer: ");
    }
    while (n >= 0);
    return n;
}
