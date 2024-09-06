#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 누적합(기억)

int main()
{
	int n;
	cin >> n;

	vector<vector<int>> graph;
	for (int i = 0; i < n; i++)
	{
		int x, y;
		vector<int> tmp(2, 0);
		
		cin >> x >> y;

		tmp[0] = x;
		tmp[1] = y;

		graph.push_back(tmp);
	}

	int max_num = 0;
	vector<int> board(1001, 0);

	int l_m_idx = 0;
	int h_m_idx = 0;

	for (auto i : graph)
	{
		board[i[0]] = i[1];

		// 최댓값이 여러개일 경우 가장 처음 나오는 인덱스
		if (i[1] > max_num)
		{
			max_num = i[1];
			l_m_idx = i[0];
		}
		// 최댓값이 여러개일 경우 가장 나중에 나오는 인덱스
		if (i[1] == max_num)
			h_m_idx = i[0];
	}

	int low_idx = 0;
	int high_idx = 1000;

	int answer = 0;
	int low_max = 0;
	int high_max = 0;

	// 낮은 인덱스부터 최대값까지 누적합 구하기
	while (low_idx != l_m_idx)
	{
		if (board[low_idx] > low_max)
			low_max = board[low_idx];

		answer += low_max;
		low_idx++;
	}
	// 높은 인덱스부터 최대값까지 누적합 구하기
	while (high_idx != h_m_idx)
	{
		if (board[high_idx] > high_max)
			high_max = board[high_idx];

		answer += high_max;
		high_idx--;
	}

	answer += (h_m_idx - l_m_idx + 1) * max_num;

	cout << answer;
}