# include<stdio.h>
# include<stdlib.h>

int main(void)
{
    int i;
    int sum = 0;

    for(i=1; i<10; ++i)
    {
        sum = sum + i;;
        printf("%d\n", sum); 
    }

    printf("sum = %d\n", sum);

    system("pause");

    return 0;
}