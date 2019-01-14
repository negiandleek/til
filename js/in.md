```js
const a = ["a", "b", "c"];
console.log(0 in a); // true
console.log("0" in a); // true

const b = {a: "A", b: "B"};
console.log("0" in b); // false
console.log("a" in b); // true
```
