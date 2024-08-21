// 14232. 보석 도둑
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    // 소인수분해를 하는 문제
    long long n;
    cin >> n;

    // 수가 매우 크므로 long long을 사용한다.
    vector<long long> vec;

    // n을 사용하게 되면 for문에서 값이 계속 바뀌므로
    // n을 복사한 x를 사용한다.

    long long x = n;
    for (long long i = 2; i * i < n + 1; i++)
    {
        // 소인수 분해를 계속해, 값을 vec에 넣어준다.
        while (x % i == 0)
        {
            vec.push_back(i);
            x /= i;
        }
    }

    // 만약 모든 소인수 분해를 마쳤는데도, x가 1이 아니라면
    // 마지막 수가 소수인 것이므로, x를 넣어준다.
    if (x != 1) vec.push_back(x);

    cout << vec.size() << "\n";
    for (auto ele : vec) cout << ele << " ";

    return 0;
}