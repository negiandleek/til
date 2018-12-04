# Trait
# Basic
```scala
{
  trait Animal[A]{
    val name: A;
    def walk(step:Int): A;
  }
  
  class Horse(val name: String) extends Animal[String]{
    override def walk(step: Int) = {
      println(name + " walk " + step + "m")
      step + "m"
    }
  }
  
  val tom = new Horse("tom");
  // tom.walk(4);
}
```
# Subtyping
```scala
trait Animal{
  val name: String
}
class Horse(val name: String) extends Animal;
class Monkey(val name: String) extends Animal;

val zebra = new Horse("zebra");
val gorilla = new Monkey("gorilla");

```
