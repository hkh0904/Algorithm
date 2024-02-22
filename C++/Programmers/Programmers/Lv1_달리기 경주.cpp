#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    vector<string> answer = players;
    unordered_map<string, int> playerIndex;

    // 선수들의 위치를 map에 저장
    for (int i = 0; i < players.size(); ++i) {
        playerIndex[players[i]] = i;
    }

    // callings를 순회하며 선수의 위치 변경
    for (const string& calling : callings) {
        int idx = playerIndex[calling];
        // 1등이 불리는 경우가 없으므로 인덱스가 0보다 작은 경우는 고려X
        if (idx > 0) {
            // 현재 선수와 바로 앞의 선수를 교체
            swap(answer[idx], answer[idx - 1]);
            // map에서도 위치 정보를 업데이트
            playerIndex[calling] = idx - 1;
            playerIndex[answer[idx]] = idx;
        }
    }

    return answer;
}


// 오답 코드

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