# Basic Simple
```ts
/* basic type */
const num: number = 0;
const str: string = "a";
const ary: number[] = [1,2,3];
const ary2: Array<number> = [1];
const tuple: [number, number, string, Object] = [1,2,"a", {}];

enum Color {blue=2, red, green};
const color = Color.red; //2

let any: any = "hoge"
any = 0;
any.test(); //compile時にはエラーにならない。実行時にエラーになる
const any2: any = [1,2,3];

let vsObject: Object = {};
vsObject.test = "test" //error
vsObject.test(); //error

const declareNull: null = null;
const declareUndefined: undefined = undefined;

const obj: Object = {a: "a", b: 0, c: []};
const obj2: Object = [1,2,{}];
const obj3: Object = new String("a");

function returnVoid(): void{}

function returnNever(): never{
	throw new Error();
}

function returnNestNever(): never{
	return returnNever();
}
```

# Array
```typescript
const arr: number[] = [1,2,3];
const arrStrAndNum: [string, number] = ["str", 0];
function getVariadic(first: (string|number), ...tail: (string|number)[]): void {
    console.log(first, tail);
}
getVariadic("a", 0, "b");

const arr: [...number[]] = [1, 2, 3];
```
