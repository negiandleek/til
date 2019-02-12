[ABC081A - Placing Marbles](https://atcoder.jp/contests/abs/tasks/abc081_a)
```c++
#include <cstdio>
using namespace std;
int main(void){
    char x[3];
    scanf("%s", x);
    int y = 0;
    for(int i = 0; i < 3; i+=1){
        if((x[i] - '0') == 1){
            y++;
        }
    }
    printf("%d", y);
}

```
