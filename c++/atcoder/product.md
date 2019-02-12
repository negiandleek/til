[ABC086A - Product](https://atcoder.jp/contests/abs/tasks/abc086_a)
```c++
#include <cstdio>
using namespace std;
int main(void){
    int x;
    int y;
    scanf("%d %d", &x, &y);
    int z = x * y;
    if(z % 2 == 0){
        printf("Even");
    }else{
        printf("Odd");
    }
}
```
