[Object.create()](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Object/create)
```js
const obj = {a: "a", b: "b"};
const createdObj = Object.create(obj);
createdObj.a = "A";
console.log(JSON.stringify(obj) === JSON.stringify(createdObj)); //false
console.log(createdObj.__proto__.a === "a"); //true

class User{
  constructor(){
    this.list = {}
  }
  add(key, name){
    if(!this.list[key]){
      this.list[key] = name;
    }
  }
}

const user = new User();
user.add("first", "tanaka");
user.add("constructor", "sato"); // can't add
console.log(user.list); // {first, "tanaka"};

class BetterUser{
  constructor(){
    this.list = Object.create(null);
  }
  add(key, name){
    if(!this.list[key]){
      this.list[key] = name;
    }
  }
}

const betterUser = new BetterUser();
betterUser.add("first", "tanaka");
betterUser.add("constructor", "sato"); // can't add
console.log(betterUser.list); // {first, "tanaka", constructor: "sato"};
```
