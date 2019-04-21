```js
function sum(x) {
    return (y) => x * y;
}

const func: (x: number) => (y: number) => number = sum
console.log(func(2)(3)) //6
```

```js
interface Sum{
    (x: number): (y: number) => number
}

function sum(x: number):(y:number) => number {
    return (y: number) => x * y;
}
const func: Sum = sum; //6
```
