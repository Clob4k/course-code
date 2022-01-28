# include<stdio.h>
# include<stdlib.h>

int main(void)
{
    if (1 > 2)
        printf("AAAA\n");             // if & else 只能影响其下一行 加括号影响括号内
    else
        {
            printf("BBBB\n");         // "{}"内的同else条件输出
            printf("CCCC\n");
        }
    printf("DDDD\n");             // else下一行后未加括号不受else影响 正常输出         

    system("pause");

    return 0;
}