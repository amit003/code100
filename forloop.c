#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    int a, b;
    scanf("%d\n%d", &a, &b);
    
    char lab[11][6] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "even", "odd"};
    int labin;
      for (int i=a; i<=b; i++) {
        labin = i <= 9 ? i - 1 : 9 + i % 2;
        printf("%s\n", lab[labin]);
    }

    return 0;
}