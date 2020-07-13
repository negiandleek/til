// A <: B
// 変数
interface Named{
  name: string
  age?: number
}
let x: Named = { name: 'John' }
let y = { name: 'Alice', location: 'Seattle' }
y = x // Error
x = y // OK

// 戻り値
let m = () => ({ name: "Alice" })
let n = () => ({ name: "Alice", location: "Seattle" })
m = n
n = m // Error

// A :> B
// パラメータ
let a = (a: number) => 0
let b = (b: number, c: string) => 0

b = a // OK
a = b // Error
