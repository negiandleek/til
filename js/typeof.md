# null
```js
const a = null;
typeof a; //object;
```
なので
```js
const a = {};

function isObject(value){
  return typeof value == "object" && value !== null
};

isObject(a) //true
```
