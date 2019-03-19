```scala
def hoge[T](x: T, length: Int): List[T] = {
  if (length < 1)
    Nil
  else
    x :: hoge(x, length - 1)
}
println(hoge[Int](3, 4))  // List(3, 3, 3, 3)
println(hoge("La", 8))
```
