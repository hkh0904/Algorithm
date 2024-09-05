#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// ������(���)
// ��ǻ�Ϳ��� ����ϴ� ����� �˷��ֱ�

int main()
{
	int a;
	cin >> a;

	vector<int> nums;
	for (int i = 0; i < a; i++)
	{
		int tmp;
		cin >> tmp;
		nums.push_back(tmp);
	}

	// nums[0] ���� �ʱⰪ ����
	int answer = nums[0];

	// ��� �������ϸ鼭 ���ư��ٰ� ���� ������ ���ͼ� �������� �۾���
	// ���� �� ��������� ���� �����պ��� ũ�ٸ� �ʱ�ȭ
	vector<int> prefix(1, 0);
	for (int i = 0; i < a; i++)
	{
		prefix.push_back(max(prefix[i] + nums[i], nums[i]));
		answer = max(answer, prefix[i + 1]);
	}

	cout << answer;
}