#include <iostream>
#include <stdlib.h>
#include<map>

# define CHAR_SIZE 128


using namespace std;

class Trie
{
public:
    bool isLeaf;
    Trie* Character[CHAR_SIZE];
    
    // constructor
    Trie()
    {
        this->isLeaf = false;

        for(int i = 0; i < CHAR_SIZE; i++)
            this->Character[i] = nullptr;
    }

    void insert(std::string);
    bool deletion(Trie*&, std::string);
    bool search(std::string);
    bool haveChildren(Trie const*);
};

void Trie::insert(string key)
{
    // start from root node
    Trie* curr = this;
    for (int i = 0; i < key.length(); i++)
    {
        // create a new node if path doesn't exists
        if (curr->Character[key[i]] == nullptr)
            curr->Character[key[i]] = new Trie();
        
        // go to the next node
        curr = curr->Character[key[i]];
    }
    curr->isLeaf = true;
}

bool Trie::search(string key)
{
    // return false if Trie is empty
    if (this == nullptr) return false;

    Trie* curr = this;
    for (int i = 0; i < key.length(); i++)
    {
        curr = curr->Character[key[i]];

        if (curr == nullptr) return false;
    }
    return curr->isLeaf;
}

bool Trie::haveChildren(Trie const* curr)
{
    for (int i = 0; i < CHAR_SIZE; i++)
    {
        if (curr->Character[i]) return true;
    }
}

bool Trie::deletion(Trie*& curr, std::string key)
{
    if (curr == nullptr) return false;

    // if we have not reached the end of the key

    if (key.length())
    {
        if (curr != nullptr &&
        curr->Character[key[0]] != nullptr &&
        deletion(curr->Character[key[0]], key.substr(1)) &&
        curr->isLeaf == false)
        {
            if (!haveChildren(curr))
            {
                delete curr;
                curr = nullptr;
                return true;
            }
            else{
                return false;
            }
        }
    }


    // if we have reached the end of the key
    if (key.length() == 0 && curr->isLeaf)
    {
        // if current node is a leaf node and do not have any children
        if (!haveChildren(curr))
        {
            delete curr;
            curr = nullptr;
            return true;
        }
        else
        {
            curr->isLeaf = false;
            return false;
        } 
    }

    return false;
}

int main()
{
    Trie* head = new Trie();

    head->insert("hello");

    std::cout << head->search("hello") << " ";


}


