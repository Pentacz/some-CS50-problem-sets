#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image");
        return 1;
    }

    // remember filename
    char *card = argv[1];

    // open infile
    FILE *inptr = fopen(card, "r");
    if (card == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", card);
        return 2;
    }

    unsigned char buffer[512];
    int i = 0;
    char filename[8];
    FILE *file = NULL;

    while (fread(buffer, 512, 1, inptr) != 0)
    {
        // start of new jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // close if already found jpeg
            if (i > 0)
            {
                fclose(file);

            }
            // if haven't found jpeg / after close file
            sprintf(filename, "%03i.jpg", i);
            file = fopen(filename, "w");
            fwrite(buffer, 512, 1, file);
            i++;
        }
        // if not start of new jpeg
        else
        {
            // if already found jpeg
            if (i > 0)
            {
                fwrite(buffer, 512, 1, file);
            }
        }
    }
    fclose(inptr);
    fclose(file);
    return 0;
}