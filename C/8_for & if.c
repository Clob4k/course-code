# include<stdio.h>
# include<stdlib.h>

int main(void)
{
    int i;
    int sum = 0;

    for(i=3; i<12; ++i)
    {
        if (i%3 == 0)           //如果i能被3整除
        {
            sum = sum + i;
            printf("%d\n", sum);
        }
    }

    printf("sum = %d\n", sum);

    system("pause");

    return 0;
}