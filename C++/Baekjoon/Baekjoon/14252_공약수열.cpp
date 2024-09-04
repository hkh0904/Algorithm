#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 완전탐색
// 정수론 (공약수)

// 두 수를 비교해서 최대공약수가 1이라면 OK
// 두 수를 비교해서 최대공약수가 1이 아니라면 NOK

// 숫자 하나 추가하거나 또는 두개를 추가한다.


int Gcd(int a, int b)
{
	while (a % b != 0)
	{
		int tmp = a % b;
		a = b;
		b = tmp;
	}
	return b;
}

int main()
{
	int answer = 0;
	int n;
	cin >> n;

	vector<int> num;
	for (int i = 0; i < n; i++)
	{
		int tmp;
		cin >> tmp;
		num.push_back(tmp);
	}

	sort(num.begin(), num.end());

	for (int i = 0; i < n - 1; i++)
	{
		if (Gcd(num[i], num[i + 1]) == 1)
			continue;

		for (int j = num[i] + 1; j < num[i + 1]; j++)
		{
			if (Gcd(num[i], j) == 1 && Gcd(j, num[i + 1]) == 1)
			{
				answer++;
				break;
			}
			if (j == num[i + 1] - 1)
				answer += 2;
		}
	}

	cout << answer;
}