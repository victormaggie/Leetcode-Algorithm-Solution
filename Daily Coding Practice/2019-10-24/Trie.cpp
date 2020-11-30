#include <iostream>
#include <string>
#define ALPHABET_SIZE 26
using namespace std;

typedef struct TrieNode
{
    int count;           // count number
    TrieNode * children[ALPHABET_SIZE];   // children
} * trie;

TrieNode* create_trie_node()
{
    TrieNode* pNode = new TrieNode;
    pNode->count = 0;
    for(int i = 0; i < ALPHABET_SIZE; i++)
    {
        pNode->children[i] = NULL;
    }
    return pNode;
};

void trie_insert(trie root, char* key)
{
    TrieNode* node = root;
    char* p = key;
    while(*p)
    {
        if (node->children[*p-'a']==NULL)
        {
            node->children[*p-'a'] = create_trie_node();
        }
        node = node->children[*p-'a'];
        ++p;
    }
    node->count += 1;
}

int trie_search(trie root, char* key)
{
    TrieNode* node = root;
    char* p = key;
    while(*p && node!= NULL)
    {
        node = node -> children[*p-'a'];
        ++p;
    }
    if (node == NULL)
        return 0;
    else
    {
        return node -> count;
    }
    
};
