#include<stdio.h>
int main()
{
    char letter;
    printf("Enter a letter : ");
    scanf("%c",&letter);
    if(letter=='a'||letter=='e'||letter=='i'||letter=='o'||letter=='u')
    {
        printf("The letter is vowel");
    }
    else
    {
        printf("The letter is not vowel");
    }
}
