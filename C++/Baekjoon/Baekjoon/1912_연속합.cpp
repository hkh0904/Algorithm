#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 누적합(기억)
// 컴퓨터에게 기억하는 방법을 알려주기

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

	// nums[0] 으로 초기값 설정
	int answer = nums[0];

	// 계속 누적합하면서 나아가다가 만약 음수가 나와서 누적합이 작아짐
	// 현재 수 더해줘야할 수가 누적합보다 크다면 초기화
	vector<int> prefix(1, 0);
	for (int i = 0; i < a; i++)
	{
		prefix.push_back(max(prefix[i] + nums[i], nums[i]));
		answer = max(answer, prefix[i + 1]);
	}

	cout << answer;
}