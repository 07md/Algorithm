#include <iostream>

using namespace std;

int main() {
	int n, m, start, end, weight, graph[107][107];
	while(cin >> n && n != 0) {
       for(int i = 1; i <= n; i ++)
           for(int j = 1; j <= n; j ++)
               graph[i][j] = 9999;
		
		for(start = 1; start <= n; start++) {
			cin >> m;
			while(m--) {
				cin >> end >> weight;
				graph[start][end] = weight;
			}
		}
		
		for(int k = 1; k <= n; k++) {
			for(int i = 1; i <= n; i++) {
				for(int j = 1; j <= n; j++) {
					if(graph[i][j] > graph[i][k] + graph[k][j]) {
						graph[i][j] = graph[i][k] + graph[k][j];
					}
				}
			}
		}
		
		int sum, stockbroker, time = 9999;
		for(int i = 1; i <= n; i++) {
			sum = 0;
			for(int j = 1; j <= n; j++) {
				if(i != j && graph[i][j] > sum) {
					sum = graph[i][j];
				}
			}
			if(sum < time) {
				stockbroker = i;
				time = sum;
			}
		}
		cout << stockbroker << " " << time << endl;
	}
	return 0;
}
