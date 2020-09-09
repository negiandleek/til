#include <stdio.h>
int main(void){
    char b = 'a' + 1;
    printf("%c\n", b);
    char hoge[] = "hoge";
    printf("%s\n", hoge);
    char fuga[21];
    strcpy(fuga, hoge);
    printf("%s\n", fuga);
    
    char piyo[256] = "piyo";
    strcat(piyo, fuga);
    printf("%s\n", piyo);
}
