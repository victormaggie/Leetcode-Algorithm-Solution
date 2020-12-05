
#include <queue>
using namespace std;

class HitCounter {
	
public:
	queue<int> q;
	HitCounter(){
		
	}
	
	void hit(int timestamp){
		q.push(timestamp);
	}
	
	int getHits(int timestamp) {
		
		while (!q.empty() && timestamp - q.front() >= 300) {
			q.pop()
		}
		return q.size();
	}
};

// use the queue to store the data