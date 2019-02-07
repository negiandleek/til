```scala
import scala.util.Random
object Id {
  def apply(str: String): String = {
    val random = new Random().nextInt(10)
    s"$str--$random"
  }
  def unapply(str: String): Option[String] = {
    val r = str.split("--")
    if(!r.isEmpty) Some(r.head) else None;
  }
}

val id = Id("id")
println(id) //id--%number%
id match {
  case Id(name) => println(name) //id
  case _ => println("Other")
}
```
