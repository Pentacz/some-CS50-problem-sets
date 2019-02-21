// Creates 2 mario-like piramids
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Asks for height
    int h;
    do
    {
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);
    
    // Prints hashes
    for (int i = 0; i < h; i++)
    {
        for (int k = i; k < h - 1; k++)
        {
            printf(" ");
        }
        for (int j = -1; j < i; j++)
        {
            printf("#");
        }
        for (int l = 1; l < 2; l++)
        {
            printf("  ");
        }
        for (int z = h - i - 1; z < h; z++)
        {
            printf("#");
        }
        printf("\n");
    }       
}
