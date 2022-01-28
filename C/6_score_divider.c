# include<stdio.h>
# include<stdlib.h>

int main(void)
{
    float score;

    printf("please type in your score\n");                

    scanf("%f", &score);

    if (score > 100)
        printf("wake up! it's morning.\n");
    else if (score >= 90)
        printf("excellent\n");
    else if (score >= 80)
        printf("good\n");
    else if (score >= 60)
        printf("pass\n");
    else if (score >= 0)
        printf("flunk\n");
    else
        printf("your score is to o low, but don't be so sad.\n");
        
    system("pause");

    return 0;
}

/*
另一种表达方式
if (score > 100)
		printf("这是做梦!\n");
	else if (score>=90 && score<=100) //不能写成 90<=score<=100
		printf("优秀!\n");
	else if (score>=80 && score<90)
		printf("良好!\n");
	else if (score>=60 && score<80)
		printf("及格!\n");
	else if (score>=0 && score<60)
		printf("不及格! 继续努力!\n");
	else
		printf("输入的分数过低，不要如此自卑!\n");
*/