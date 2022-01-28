# include<stdio.h>
# include<stdlib.h>

int main(void)
{
    double delta;

    printf("delta =");
    scanf("%d", &delta);

    if (delta > 0)
        printf("two real root\n");
    else if (delta == 0)
        printf("one real root\n");
    else
        printf("none real root\n");

    system("pause");

    return 0;
}