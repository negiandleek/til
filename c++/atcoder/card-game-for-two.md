[ABC088B - Card Game for Two](https://atcoder.jp/contests/abs/tasks/abc088_b)
```c++
#include <cstdio>

using namespace std;
int main(void){
    int len;
    scanf("%d", &len);
    int arr[len];
    int count = 0;
    int a = 0;
    int b = 0;
    for(int i = 0; i < len; i += 1){
        int n;
        scanf("%d", &n);
        arr[i] = n;
    }
    
    for(int i = 0; i < len - 1; i += 1){
        for(int j = 0; j < len - (1 + i); j += 1){
            if(arr[j] - arr[j + 1] < 0){
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }   
        }
    }
    
    while(true){
        if(count >= len) break;
        if(count % 2 == 0){
            a += arr[count];
        }else{
            b += arr[count];
        }
        count += 1;
    }
    
    printf("%d", a - b);
}
```
