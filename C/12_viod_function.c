# include<stdio.h>
# include<stdlib.h>

void Max(int i, int j)                                 
{
    if (i > j)
        printf("%d\n", i);
    else
        printf("%d\n", j);
}

int main(void)
{
    int a, b, c, d, e, f;

    a = 1, b = 2, c =3, d = 9, e = -5, f = 100;
    Max(a,b);
    Max(c,d);
    Max(e,f); 

    system("pause");

}