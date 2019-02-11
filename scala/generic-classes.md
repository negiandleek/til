```scala
class CustomList[A] {
  private var elements: List[A] = Nil;
  def push(elm: A) = elements = elm::elements
  def get(): List[A] = elements
}

val list = new CustomList[Int];
list.push(10)
list.push(2)
println(list.get())
```
