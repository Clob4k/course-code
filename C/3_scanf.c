# include <stdio.h>
# include <stdlib.h>

int main(void)
{
    int i, j;

    scanf("%d", &i);                            //不含输入控制符的用法
    printf("i = %d\n", i);

    scanf("n%d", &i);                           //含有输入控制符的用法
    printf("i = %d\n", i);

    scanf("%d %d", &i, &j);                     //一次给多个变量赋值        
    printf("i = %d, j = %d\n", i, j);

    system("pause");

    return 0;
}