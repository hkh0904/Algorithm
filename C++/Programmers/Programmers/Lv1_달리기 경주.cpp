#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    vector<string> answer = players;
    unordered_map<string, int> playerIndex;

    // �������� ��ġ�� map�� ����
    for (int i = 0; i < players.size(); ++i) {
        playerIndex[players[i]] = i;
    }

    // callings�� ��ȸ�ϸ� ������ ��ġ ����
    for (const string& calling : callings) {
        int idx = playerIndex[calling];
        // 1���� �Ҹ��� ��찡 �����Ƿ� �ε����� 0���� ���� ���� ���X
        if (idx > 0) {
            // ���� ������ �ٷ� ���� ������ ��ü
            swap(answer[idx], answer[idx - 1]);
            // map������ ��ġ ������ ������Ʈ
            playerIndex[calling] = idx - 1;
            playerIndex[answer[idx]] = idx;
        }
    }

    return answer;
}


// ���� �ڵ�

//void Change(vector<string>* runners, string splinter)
//{
//    auto it = find(runners->begin(), runners->end(), splinter);
//    int idx = distance(runners->begin(), it);
//
//    string temp = (*runners)[idx];
//    (*runners)[idx] = (*runners)[idx - 1];
//    (*runners)[idx - 1] = temp;
//}
//
//
//vector<string> solution(vector<string> players, vector<string> callings) {
//    vector<string> answer = players;
//
//    int len = callings.size();
//
//    for (int i = 0; i < len; i++)
//    {
//        Change(&answer, callings[i]);
//    }
//
//    return answer;
//}