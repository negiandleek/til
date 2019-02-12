[ABC081B - Shift only](https://atcoder.jp/contests/abs/tasks/abc081_b)
```c++
#include <cstdio>
using namespace std;
int main(void){
    int size;
    scanf("%d", &size);
    int nums[size];
    int count = 0;
    
    for(int i = 0; i < size; i += 1){
        int temp;
        scanf("%d\n", &temp);
        nums[i] = temp;
    }
    
    while(true){
        bool flag = true;
        for(int i = 0; i < size; i += 1){
            if(nums[i] % 2 == 0){
                nums[i] = nums[i] / 2;
            }else{
                flag = false;
                break;
            }
        }
        if(flag == false){
            break;   
        }
        count++;
    }
    printf("%d", count);
}

```
