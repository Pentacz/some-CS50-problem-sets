// Julius Caesar cipher!
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // Checks if there are two arguments or strings
    if (argc == 2)
    {
        // Iterates for each character in argv 
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            // Checks if every character in argv is digit
            if (isdigit(argv[1][i]))
            {
            }
            else
            {
                printf("Usage: ./caesar key\n");
                return 2;
            }
        }
        // Changes argv from character to integer
        int j = atoi(argv[1]);
        // Prompting for plaintext
        string pt = get_string("plaintext: ");
        printf("ciphetext: ");
        // Dummy protection to not exceed ASCII table
        while (j >= 26)
        {
            j = j - 26;
            
        }
        // Iterates each character in plaintext
        for (int k = 0; k < strlen(pt); k++)
        {
            // Ciphers uppercase letters
            if (pt[k] >= 'A' && pt[k] <= 'Z')
            {
                // Protection against going out of letters
                if (pt[k] + j > 'Z')
                {
                    printf("%c", pt[k] - 26 + j);
                }
                else
                {
                    printf("%c", pt[k] + j);
                }
            }
            // Ciphers lowercase letters
            else
            {
                if (pt[k] >= 'a' && pt[k] <= 'z')
                {
                    // Again, protection against going out of letters
                    if (pt[k] + j > 'z')
                    {
                        printf("%c", pt[k] - 26 + j);
                    }
                    else
                    {
                        printf("%c", pt[k] + j);
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
        printf("Usage: ./caesar key\n");
        return 1;
    }
}
