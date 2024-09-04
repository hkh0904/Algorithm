#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 누적합(기억)
// 컴퓨터에게 기억하는 방법을 알려주기



int main()
{
	int answer;

	int a, b;
	cin >> a >> b;

	vector<int> nums;
	for (int i = 0; i < a; i++)
	{
		int tmp;
		cin >> tmp;
		nums.push_back(tmp);
	}

	vector<int> prefix(1, 0);
	for (int i = 0; i < a; i++)
		prefix.push_back(prefix[i] + nums[i]);

	vector<int> chk;
	for (int i = b; i < a + 1; i++)
		chk.push_back(prefix[i] - prefix[i - b]);

	auto ans = max_element(chk.begin(), chk.end());
	answer = *ans;

	cout << answer;
}