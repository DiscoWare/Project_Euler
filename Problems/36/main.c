#include "double_base.h"

int main()
{
    int sum = 0;
    for (int i = 0; i < 1000000; ++i)
    {
        if (is_bin_pal(i) && is_dec_pal(i))
        {
            printf("%d\n", i);
            sum += i;
        }
    }
    printf("sum: %d\n", sum);

    return 0;
}