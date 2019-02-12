[A - はじめてのあっとこーだー](https://atcoder.jp/contests/practice/tasks/practice_1)
```c++
#include <cstdio>
using namespace std;
int main(void){
    int x;
    int y;
    int z;
    char str[100];
    scanf("%d", &x);
    scanf("%d %d", &y, &z);
    scanf("%s", str);
    
    printf("%d %s\n", x + y + z, str);
}

```
