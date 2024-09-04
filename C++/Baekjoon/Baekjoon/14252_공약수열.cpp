#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// ����Ž��
// ������ (�����)

// �� ���� ���ؼ� �ִ������� 1�̶�� OK
// �� ���� ���ؼ� �ִ������� 1�� �ƴ϶�� NOK

// ���� �ϳ� �߰��ϰų� �Ǵ� �ΰ��� �߰��Ѵ�.


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