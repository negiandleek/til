# Infinity
参考: [Object.isのpolyfill](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Object/is#Polyfill)
```js
const i = 1 / +0; // Infinity
const j = 1 / -0; // -Infinity
i === j //false
```
