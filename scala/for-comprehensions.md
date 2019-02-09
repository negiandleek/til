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
