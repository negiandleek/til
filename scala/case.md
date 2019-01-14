```scala
import scala.util.Random

val x: Int = Random.nextInt(10)

val r = x match {
  case 0 => "zero"
  case 1 => "one"
  case 2 => "two"
  case _ => "many"
}

def func(y: Int) = y match {
  case 0 => "zero"
  case 1 => "one"
  case 2 => "two"
};
```
