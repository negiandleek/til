```js
const hoge = function(){
  this.a = "a"
};
hoge.prototype.b = "b";

const fuga = new hoge();

console.log(fuga.hasOwnProperty("a")); //true
console.log(fuga.hasOwnProperty("b")); //false
```
