```js
const Hoge = function(){};
const hoge = new Hoge();

console.log(Hoge.constructor === Function) //true
console.log(hoge.constructor === Hoge) // true
```
