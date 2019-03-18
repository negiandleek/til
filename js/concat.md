```js
let state = [{name: "dio"}];
let newState = [].concat(state[0]);
state[0].name = "giorno";
console.log("newState", newState); //"newState", {[name: "giorno]};
newState[0].name = "jotaro";
console.log(state); //"state", {[name: "jotaro"]};
```
