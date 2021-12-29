#include <iostream> 

using namespace std;

int gcd(int a, int b) {
	return b == 0 ? a : gcd(b, a % b);
}

int main() {
	int ans = 0;
	for (int i = 1; i < 2021; i++) {
		for (int j = 1; j < 2021; j++) {
			if (i != j && gcd(i, j) == 1) {
				ans += 1;
			}
		}
	}
	cout << "ans = " << ans << endl;
	return 0;
}
