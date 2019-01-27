```scala
import scala.util.matching.Regex

val nameReg: Regex = "([A-Z][a-z].+)([A-Z][a-z].+)".r;
val r = "WilliamSmith" match {
  case nameReg(x, y) => println(x, y);
  case _ => println("None")
}

// William,Smith
```

```scala
val input = """
  WilliamSmith
  MaryTaylor
"""

for(matched <- nameReg.findAllMatchIn(input))
  println(matched.group(1), matched.group(2))
  
// William,Smith
// Mary,Taylor
```
