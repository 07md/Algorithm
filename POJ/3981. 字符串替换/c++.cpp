#include <string>
#include <iostream> 

using namespace std;

int main() {
	string str;
	while (getline(cin, str)) {
		while (str.find("you") != string::npos)
			str.replace(str.find("you"), 3, "we");
		cout << str << endl;
	}
	return 0;
}
