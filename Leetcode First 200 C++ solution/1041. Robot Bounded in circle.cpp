#include <string>
#include <iostream>
using namespace std;
class Solution {
public:
    bool isRobotBounded(string s) {
        
        // distance
        int x = 0;
        int y = 0;
        // heading
        int dx = 0, dy = 1;
        
        for(int i = 0; i < s.size(); i++){
            
            cout << s[i] << endl;
            string dir = s[i];
            
            if (dir == 'G'){
                x = x + dx;
                y = y + dy;
            } else if (dir == 'L') {
                int tmp = dy;
                dy = dx;
                dx = -tmp;
            } else {
                int tmp = dx;
                dx = dy;
                dy = -tmp;
            }
        }
        
        return (x == 0 && y == 0) }} dy != 1;
        
    }
};