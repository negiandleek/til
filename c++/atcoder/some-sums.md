[ABC083B - Some Sums](https://atcoder.jp/contests/abs/tasks/abc083_b)
```c++
#include <iostream>
using namespace std;
int main(void){
    // Your code here!
    int n;
    int a;
    int b;
    int total = 0;
    
    scanf("%d", &n);
    scanf("%d", &a);
    scanf("%d", &b);
    
    for(int i = 0; i <= n; i += 1){
        int x = i;
        int y = 0;
        while(x > 0){
            y += (x % 10);
            x = x / 10;
        }
        if(a <= y && y <= b){
            total += i;
        }
    }
    printf("%d", total);
}
```
