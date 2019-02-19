#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
float x;     
do
{
x = get_float("Change owed: ");
}
while (x < 0);
int i = round(x * 100);
int a = 0;
int b = 0;
int c = 0;
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

