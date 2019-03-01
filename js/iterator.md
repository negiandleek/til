iteratorは`next()メソッド`と`iterator result`を持つ  
iterator resultはオブジェクトで、`value`と、`done`プロパティを持つ
  
```js
const obj = {};
obj[Symbol.iterator] = function(){
  const iterator = {};
  let count = 1;
  iterator.next = () => {
    count = count * 2;
    return count <= 16
      ? {value: count, done: false}
      : {done: true}
  }
  return iterator;
}

const iterator = obj[Symbol.iterator]();
// console.log(iterator.next()); // 2

for(const entry of obj){
  console.log(entry) // 2 4 8 16
}
```
