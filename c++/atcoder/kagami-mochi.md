[ABC085B - Kagami Mochi](https://atcoder.jp/contests/abs/tasks/abc085_b)
```c++
#include <cstdio>
using namespace std;
int main(void){
    int n;
    scanf("%d", &n);
    int arr[n];
    int prevMax = 101;
    int count = 0;
    
    for(int i = 0; i < n; i += 1){
        int a;
        scanf("%d\n", &a);
        arr[i] = a;
    }
    
    for(int i = 0; i < n; i += 1){
        int max = 0;
        for(int j = 0; j < n; j += 1){
            if(max < arr[j] && arr[j] < prevMax){
                max = arr[j];
            }
        }
        if(max == 0) break;
        prevMax = max;
        count += 1;
    }
    
    printf("%d", count);
}
```
