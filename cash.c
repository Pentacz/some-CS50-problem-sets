// Asks for change and prints min nbr of coins
#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(int argc, string argv[])
{
    // Gets change owed
    float x;     
    do
    {
        x = get_float("Change owed: ");
    }
    while (x < 0);
    // Counts quarters, dimes and nickels needed
    int i = round(x * 100);
    int a = 0, b = 0, c = 0;
    while (i >= 25)
    {
        i = i - 25; a++;
    }
    while (i >= 10)
    {
        i = i - 10; b++;
    }
    while (i >= 5)
    {
        i = i - 5; c++;
    }
    printf("%i\n", a + b + c + i);
}

