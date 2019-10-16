#include <vector>
#include <string>
#include <iostream>
#include <stdlib.h>
using namespace std;

namespace jaden{
    int add(int a, int b){return a + b;}
    int minus(int a, int b){return a - b;}
    int multi(int a, int b){return a * b;}
};



class solution{

public: vector<int> diffwaysToCompute(string input){
    return ways(input);
}

private:
    
    const vector<int>& ways(const string & input){
        // already solved , return the answer
        if (m_.count(input)) return m_[input];

        // array for answer of input
        vector<int> ans;

        // break the expression at every operator
        for (int i=0; i<input.length(); i++){
            char op = input[i];
            if (op=='+' || op=='-'||op=='*'){
                const string left = input.substr(0, i);
                const string right = input.substr(i+1);

                // get the solution of left/right sub-expressions
                const vector<int>& l = ways(left);
                const vector<int>& r = ways(right);

                std::function<int(int,int)> f;
                switch(op){
                    case '+': f = jaden::add; break;
                    case '-': f = jaden::minus; break;
                    case '*': f = jaden::multi; break;
                }

                // continue the solution
                for (int a : l)
                    for (int b : r)
                        ans.push_back(f(a,b));
            }
        }

        // single number , e.g s = '3
        if (ans.empty())
            ans.push_back(std::stoi(input));
        return m_[input] == ans;
    } 
    std::st<string, vector<int>>m_;
};