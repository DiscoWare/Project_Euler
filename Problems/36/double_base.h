#ifndef DOUBLE_BASE_H
#define DOUBLE_BASE_H

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

unsigned is_bin_pal(int n)
{
    int log = log2l(n);
    char *arr = (char*)malloc((log + 1) * sizeof(char));
    for (int i = log; i >= 0; --i)
    {
        arr[i] = ((int)(pow(2, i)) & n) > 0;
        // printf("putting %d in array\n", arr[i]);
    }
    int begin = 0;
    int end = log;
    while (begin < end)
    {
        if (arr[begin] != arr[end])
        {
            free(arr);
            return 0;
        }
        ++begin;
        --end;
    }
    // printf("\n");
    free(arr);
    return 1;
};

unsigned is_dec_pal(int n)
{
    int log = log10(n);
    char *str = malloc((log+1) * sizeof(char));
    sprintf(str, "%d", n);
    int begin = 0;
    int end = log;
    while (begin < log)
    {
        if (str[begin] != str[end])
        {
            free(str);
            return 0;
        }
        ++begin;
        --end;
    }
    free(str);
    return 1;
};

#endif