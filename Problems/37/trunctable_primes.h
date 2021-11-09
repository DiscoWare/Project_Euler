#include <stdio.h>
#include <stdlib.h>
#include <math.h>

unsigned int is_prime(int n)
{
    if (n < 2)
        return 0;
    for (unsigned i = 2; i * i <= n; ++i)
    {
        if (n % i == 0)
            return 0;
    }
    return 1;
}

// Does NOT check n itself
unsigned int is_l_trunctable(int n)
{
    int log = (int)log10(n);

    for (int i = log; i > 0; --i)
    {
        int div = (int)(pow(10, i) + 0.5);         // pow() can round to x.99999999, so add 0.5
        n %= div;
        if (!is_prime(n))
            return 0;
    }
    return 1;
}

// Does NOT check n itself
unsigned int is_r_trunctable(int n)
{
    int log = log10(n);
    for (int i = 1; i <= log; ++i)
    {
        n /= 10;
        if (!is_prime(n))
            return 0;
    }
    return 1;
}