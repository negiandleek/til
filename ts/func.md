```js
function sum(x) {
    return (y) => x * y;
}

const func: (x: number) => (y: number) => number = sum
console.log(func(2)(3)) //6
```
