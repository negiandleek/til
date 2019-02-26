```js
const list = [1,2,3];
const a = value => value.map(it => it * 100);
const b = value => value.reduce((memo, current) => memo + current, 0)
const r = list |> a |> b; //600
```
