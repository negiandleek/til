```scala
trait Creature{
  type T;
  def kind: List[T];
}
abstract class Animal extends Creature;

class Pet;
class InDoor extends Pet;
class OutDoor extends Pet;

val myPet = new Animal{
  type T = Pet;
  val kind = List(new InDoor, new OutDoor);
}
```

# abstract type vs generic
[stack overflow](https://stackoverflow.com/questions/1154571/scala-abstract-types-vs-generics)
