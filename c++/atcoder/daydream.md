```c++
#include <iostream>
#include <string>
using namespace std;

int main(void){
    // Your code here!
    string strList[4];
    strList[0] = "dream";
    strList[1] = "dreamer";
    strList[2] = "erase";
    strList[3] = "eraser";
    
    string answer;
    cin >> answer;
    
    int i = 0;
    int len = answer.length();
    bool flag = len == 0 ? false : true;
    while(i < len){
        string a = answer.substr(i, 7);
        if(a == strList[1]){
            string s = answer.substr(i + 7, 1);
            if(s == "a"){
                i += 5;
            }else{
                i += 7;
            }
            continue;
        }
        string b = answer.substr(i, 6);
        if(b == strList[3]){
            i += 6;
            continue;
        }
        
        string c = answer.substr(i, 5);
        if(c == strList[0] || c == strList[2]){
            i += 5;
            continue;
        }
        flag = false;
        break;
    }
    
    if(flag){
        cout << "YES" << "\n";
    }else{
        cout << "NO" << "\n";
    }
}
```
