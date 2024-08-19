#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int n;
	cin >> n;

	int chk = 1;
	int answer = 0;

	while (true)
	{
		if (chk * chk <= n)
			answer++;
		else
			break;

		chk++;
	}

	cout << answer;

}