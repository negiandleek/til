```scala
case class Student(name: String, age: Int);

val students: List[Student] = List(
  Student("hoge", 12),
  Student("fuga", 18),
  Student("piyo", 22)
);

val ageTwentyUser = for(it <- students if(it.age > 20))
  yield it.name
  
ageTwentyUser.foreach(it => println(it)) //piyo
```
```scala
def func(n: Int, m: Int) = {
  for(i <- 0 until n; j <- 0 until n; if(i + j == n))
    yield(i, j)
}

func(10, 10).foreach {
  case(i, j) => println(i, j)
}
```
