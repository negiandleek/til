```js
const arr = [
  {id: 0, value: "aaa"},
  {id: 1, value: ""},
  {id: 2, value: "ccc"}
]

!arr.some(it => Object.values(it).some(val => val === ""));
arr.every(it => Object.values(it).every(val => val !== ""));
```
