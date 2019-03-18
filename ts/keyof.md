```typescript
interface A {
    hoge: "0",
    0: "fuga"
}

type keys = keyof A;

const a: keys = "hoge"; 
const b: keys = 0;
```
