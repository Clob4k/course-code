# include <stdio.h>
# include <stdlib.h>

int main(void)
{
    int x = 47;

    printf("%x\n", x);      //输出结果为2f    
    printf("%X\n", x);      //输出结果为2F
    printf("%#x\n", x);     //输出结果为0x2f
    printf("%#X\n", x);     //输出结果为0x2F

    system("pause");
    
    return 0;
}