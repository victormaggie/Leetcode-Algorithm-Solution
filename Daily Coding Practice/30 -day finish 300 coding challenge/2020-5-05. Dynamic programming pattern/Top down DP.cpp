using namespace std;

#include<iostream>
#include<vector>

class Fibnacci{

public:
    virtual int CalculateFibonacci(int n){
        vector<int> memoize(n+1, 0);
        return CalculateFibonacciRecursive(memoize, n);
    }

    virtual int CalculateFibonacciRecursive(vector<int> &memoize, int n){
        if (n < 2){
            return n;
        }
        // if we have already solved this subproblem, simply return the result from the cache
        if (memoize[n] != 0)
            // avoid repeative calculation here
            // just return the memoize
            return memoize[n];
        
        memoize[n] = CalculateFibonacciRecursive(memoize, n-1) + CalculateFibonacciRecursive(memoize, n-2);
        return memoize[n];
    }
};

int main(int argc, char *argv[]){
    Fibnacci *fib = new Fibnacci();
    cout << '5th Fibonacci is -->' << fib->CalculateFibonacci(5) << endl;
    cout << '6th Fibonacci is -->' << fib->CalculateFibonacci(6) << endl;
    delete fib;
}

