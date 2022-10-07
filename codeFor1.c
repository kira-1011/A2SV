#include<stdio.h>
#include<string.h>

char* codeOneArray(unsigned long long int n);
char* leftArr = "";

int main()
{

    unsigned long long int n, l, r;
    unsigned int ones = 0;

    scanf("%llu, %llu, %llu",&n, &l, &r);

    char* onesArray = codeOneArray(n);

    printf(onesArray);


    return 0;
}

char* codeOneArray(unsigned long long int n)
{
    if(n == 1)
        return "1";
    
    else
    {
        leftArr = codeOneArray(n / 2);

        // leftArr += (to_string(n % 2));

        strcat(leftArr, (char *)(to_string(n % 2)));

        return leftArr;
    }   
}