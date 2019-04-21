```typescript
interface A {
    hoge: "0",
    0: "fuga"
}

type keys = keyof A;

const a: keys = "hoge"; 
const b: keys = 0;
```

```typescript
interface Type{
    hoge: string;
    fuga: number;
}

const a: Type["hoge"] = "test"
const b: Type[keyof Type] = 0;
```
