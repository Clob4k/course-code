# include <stdio.h>
# include <stdbool.h>

typedef enum {true=1,false=0}bool;

bool IsPrime(int m)
{
    int i;
    for (i=2; i<m; ++i)
    {
        if (0 == m%i)
            break;
    }
    if (i == m)
        return true;
    else
        return false;
}

void Traverseval(int n)
{
    int i;
    for (i=2; i<n; ++i)
    {
        if ( IsPrime(i) ) 
            printf("%d\n", i);
    }
}

int main(void)
{
    int val;
    int i;
    do
        {
            printf("input a number to calculate the Primes:\n");
            scanf("%d", &val);
            Traverseval(val);
                    
        } while (1);
}