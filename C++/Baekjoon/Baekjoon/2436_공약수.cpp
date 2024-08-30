#include <iostream>
#include <vector>

using namespace std;

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
	int gcd, lcm;
	cin >> gcd >> lcm;

	long long mul = gcd * lcm;
	int temp = (sqrt(mul) / gcd);
	temp *= gcd;

	int a, b;

	while (true)
	{
		if (mul % temp == 0 && Gcd(temp, mul / temp) == gcd)
		{
			a = temp;
			b = mul / temp;
			break;
		}

		temp -= gcd;
	}

	cout << a << ' ' << b;
}