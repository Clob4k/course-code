# include<stdio.h>
# include<stdlib.h>

int main(void)
{
    int val;

    printf("input a number(1~3).\n");
    scanf("%d", &val);

    switch (val)
    {
        case 1:
            printf("first.\n");
            break;
        case 2:
            printf("second.\n");
            break;
        case 3:
            printf("third.\n");
            break;
        default:
            printf("please input a number 1~3.\n");
    }

    system("pause");

    return 0;
}