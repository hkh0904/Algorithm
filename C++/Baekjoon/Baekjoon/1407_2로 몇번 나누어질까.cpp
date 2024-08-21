#include <iostream>
#include <vector>

using namespace std;

long long a, b;

long long temp(long long n)
{
    vector<long long> vec;
    long long answer = 0;
    long long i = 2;
    for (; i < n + 1; i *= 2)
    {
        vec.push_back(n / i);
    }
    vec.push_back(0);

    i /= 2;
    for (int j = vec.size() - 2; j >= 0; j--)
    {
        answer += (vec[j] - vec[j + 1]) * i;
        i /= 2;
    }
    answer += n - vec[0];

    return answer;
}


int main()
{
    cin >> a >> b;
    cout << temp(b) - temp(a - 1);

    return 0;
}
