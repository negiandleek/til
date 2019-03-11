```typescript
const a: object = { a: "a" };
const b: object = "a"; // error
const c: Object = "a"; // Object equal {}
const d: {} = "a"

function fa(value: {}): void {
    console.log(value.hoge); //error
};
function fb(value: any): void { 
    console.log(value.hoge);
};

fa({ hoge: "hoge" });
fb({ hoge: "hoge" });
```
