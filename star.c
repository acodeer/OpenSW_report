#include<stdio.h>

int main()
{
    int i = 0;
    for(i; i< 10; i++)
    {
        for(int j = 0; j < i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
}