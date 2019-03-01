# cstdio
```c++
#include <cstdio>
using namespace std;
int main(void){
    int x;
    scanf("%d", &x);
    printf("%d", x);
}
```
# iostream
```c++
#include <iostream>
using namespace std;
int main(void){
    int n;
    cin >> n;
    int a[n];
    for(int i = 0; i < n; i += 1){
        cin >> a[i];
        cout << a[i] << "\n";
    }
}
```
