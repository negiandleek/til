[ABC085C - Otoshidama](https://atcoder.jp/contests/abs/tasks/abc085_c)
```
#include <cstdio>
using namespace std;

int main() {
    int n;
    int money;
    bool flag = false;
    bool breakFlag = false;
    scanf("%d", &n);
    scanf("%d", &money);

    for(int i = 0; i <= n; i += 1){
        int a = i * 10000;
        for(int j = 0; j <= n - i; j += 1){
            int b = a + (j * 5000) + (n - (j + i)) * 1000;
            if(b == money){
                printf("%d %d %d", i, j, n - (j + i));
                breakFlag = true;
                flag = true;
                break;
            }
        }
        if(breakFlag == true) break;
    }

    if(flag == false){
        printf("%d %d %d", -1, -1,-1);
    }
}
```
