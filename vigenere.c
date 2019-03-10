// Vigenere cipher
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Declares prototype for code shift, defining at the end
int shift(char c);

int main(int argc, string argv[])
{
    // Checks if there are two arguments or strings
    if (argc == 2)
    {
        // Iterates for each character in argv 
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            // Checks if every character in argv is alphanumeric
            if (isalpha(argv[1][i]))
            {
            }
            else
            {
                printf("Usage: ./vigenere keyword\n");
                return 1;
            }
        }
        // Prompting for plaintext
        string pt = get_string("plaintext: ");
        printf("ciphertext: ");
        // Iterates each character in plaintext
        for (int k = 0; k < strlen(pt); k++)
        {
            int j = k;
            while (j >= strlen(argv[1]))
            {
                j = j - strlen(argv[1]);
            }
            // Ciphers uppercase letters
            if (pt[k] >= 'A' && pt[k] <= 'Z')
            {
                // Protection against going out of letters
                if (pt[k] + shift(argv[1][j]) > 'Z')
                {
                    printf("%c", pt[k] - 26 + shift(argv[1][j]));
                }
                else
                {
                    printf("%c", pt[k] + shift(argv[1][j]));
                }
            }
            // Ciphers lowercase letters
            else
            {
                if (pt[k] >= 'a' && pt[k] <= 'z')
                {
                    // Again, protection against going out of letters
                    if (pt[k] + shift(argv[1][j]) > 'z')
                    {
                        printf("%c", pt[k] - 26 + shift(argv[1][j]));
                    }
                    else
                    {
                        printf("%c", pt[k] + shift(argv[1][j]));
                    }
                }
                // Prints characters that aren't alphabetical
                else
                {
                    printf("%c", pt[k]);
                }
            }
        }
        printf("\n");
        return 0;
    }
    else
    {
        printf("Usage: ./vigenere keyword\n");
        return 1;
    }
}

// Implements shift: A or a = 0, B or b = 1 etc.
int shift(char c)
{
    if (isupper(c))
    {
        return c - 'A';
    }
    else
    {
        return c - 'a';
    }
}  
