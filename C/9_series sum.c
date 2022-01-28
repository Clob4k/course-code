/* 注意：循环中定义的变量不能为浮点型 wrong_eg: float sum = 0; */
# include<stdio.h>
# include<stdlib.h>

int main(void)
{
    int i;
    float sum = 0;

    for(i=1; i<=100; ++i)
    {
        if (i%3 == 0)           //如果i能被3整除
            sum = sum + 1.0/i;

    //  另一种写法
    //    sum = sum + 1 / (float)(i);         // 强制类型转换：（数据类型）（表达式）
    //                                        // 功能：把表达式的值强制转化为前面的数据类型
  
    }

    printf("sum = %f\n", sum);          //float必须用%f输出

    system("pause");

    return 0;
}