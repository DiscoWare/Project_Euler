#include <iostream>
#include <cmath>
using namespace std;

void displayDecimals(float n)
{
	float divisor = 0.1;
	cout << floor(n / divisor) << endl;
	cout << n - floor((n / divisor)) * divisor << endl;
	while (floor(n / divisor) > 0)
	{
		cout << n / divisor << endl;
		n = n - floor(n / divisor);
		divisor /= 10;
	}
}

int main()
{
	displayDecimals(1.0 / 7.0);
	return 0;
}
