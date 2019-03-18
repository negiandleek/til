```typescript
type Hoge<T> = { [K in keyof T]?: T[K] };

interface a {
    hoge: "bar";
    0: "baz"; 
};

const b: Hoge<a> = {
    0: "baz"
};
```
