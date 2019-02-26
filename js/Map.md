```js
const user = new Map();
const id = Symbol();
const id2 = Symbol();
user.set(id, "tanaka");
user.set(id2, "sato");
user.set(id2, "kato");

user.get(id); //tanaka
user.get(id2); //kato
```

# Object to Map
```js
const sample = new Map([["a",0], ["b",1]]);
const obj = {a: 0, b: 1, c: 2};
const map = new Map(Object.entries(obj));

```
