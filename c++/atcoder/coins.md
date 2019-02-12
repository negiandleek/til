[ABC087B - Coins](https://atcoder.jp/contests/abs/tasks/abc087_b)
```c++
#include <iostream>
using namespace std;
int main(void){
    // Your code here!
    int x;
    int y;
    int z;
    int total;
    int count = 0;
    scanf("%d", &x);
    scanf("%d", &y);
    scanf("%d", &z);
    scanf("%d", &total);
    
    for(int i = 0; i <= x; i += 1){
        for(int j = 0; j <= y; j += 1){
            for(int k = 0; k <= z; k += 1){
                if(i * 500 + j * 100 + k * 50 == total){
                    count++;
                }
            }
        }
    }
    printf("%d", count);
}

```
