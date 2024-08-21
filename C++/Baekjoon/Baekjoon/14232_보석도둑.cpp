// 14232. ���� ����
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    // ���μ����ظ� �ϴ� ����
    long long n;
    cin >> n;

    // ���� �ſ� ũ�Ƿ� long long�� ����Ѵ�.
    vector<long long> vec;

    // n�� ����ϰ� �Ǹ� for������ ���� ��� �ٲ�Ƿ�
    // n�� ������ x�� ����Ѵ�.

    long long x = n;
    for (long long i = 2; i * i < n + 1; i++)
    {
        // ���μ� ���ظ� �����, ���� vec�� �־��ش�.
        while (x % i == 0)
        {
            vec.push_back(i);
            x /= i;
        }
    }

    // ���� ��� ���μ� ���ظ� ���ƴµ���, x�� 1�� �ƴ϶��
    // ������ ���� �Ҽ��� ���̹Ƿ�, x�� �־��ش�.
    if (x != 1) vec.push_back(x);

    cout << vec.size() << "\n";
    for (auto ele : vec) cout << ele << " ";

    return 0;
}