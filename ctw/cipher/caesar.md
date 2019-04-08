```js
function caesar(str, shift){
    let point = str.charCodeAt(0);
    if(65 <= point && point <= 90){
        point += shift;
        if(point > 90){
            point -= 26;
        }
    }else{
        point += shift;
        if(point > 122){
            point -= 26;
        }
    }
    return String.fromCharCode(point);
}
```
