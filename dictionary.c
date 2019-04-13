// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table
node *hashtable[N];

// Hashes word to a number between 0 and 25, inclusive, based on its first letter
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}
int count = 0;

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // TODO load - Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }
    // Open dictionary and check if is not NULL
    FILE *file = fopen(dictionary, "r");
    if (!file)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {

        // Make first letter of a word an actual integer
        int h = hash(word);

        // Allocate space for word, also creating new node n
        node *n = malloc(sizeof(node));

        // Unload and return false when run out of memory
        if (!n)
        {
            unload();
            return false;
        }

        // Copy a word into node n and add counter of words
        strcpy(n->word, word);
        count++;

        // Check if there is a linked list already
        if (hashtable[h])
        {
            n->next = hashtable[h];
            hashtable[h] = n;
        }

        // Just add word when list is initially empty
        else
        {

            hashtable[h] = n;
            n->next = NULL;
        }
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO size
    return count;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // TODO check
    node *c = hashtable[hash(word)];
    while (c != NULL)
    {
        // Compare strings
        if (strcasecmp(c->word, word) == 0)
        {
            // Returns true if are the same
            return true;
        }
        else
            // Point next node
        {
            c = c->next;
        }
    }

    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO unload counts buckets (letters)
    for (int j = 0; j < N; j++)
    {
        node *c = hashtable[j];
        // Unload every node in a bucket/on that letter
        while (c != NULL)
        {
            node *temp = c;
            c = c->next;
            free(temp);
        }
    }
    return true;
}
