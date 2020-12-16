
#include<iostream>
#include<ctime>

using namespace std;

int main() {
	int time, hour, mini, sec;
	cin >> time;
	hour = time / 3600;
	mini = time / 3600 % 60;
	sec  = time % 60;
	
	cout << hour << ":" << mini << ":" << sec;
	
	return 0;
}