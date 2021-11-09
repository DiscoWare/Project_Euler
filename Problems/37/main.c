#include "trunctable_primes.h"

int main()
{
    int i = 11;
    int count = 0;
    int sum = 0;
    while (count < 11)
    {
        if (is_prime(i) && is_l_trunctable(i) && is_r_trunctable(i))
        {
            ++count;
            sum += i;
            printf("i: %d, count: %d, sum: %d\n", i, count, sum);
        }
        ++i;
    }

    return 0;
}