# Basic
```scala
case class Pet(name: String, kind: String, age: Int);
val dog = Pet("pochi", "DOG", 10);
println(dog); //Pet(pochi,DOG,10)
// dog.name = "tama" Error

val dog2 = dog.copy(name = "hachi", age = 2);
println(dog2) //Pet(hachi,DOG,2)

val dog3 = Pet("pochi", "DOG", 10);
println(dog == dog3)
```

# Case Class
```scala
abstract class Creature;

case class Fish(name: String) extends Creature;

case class Animal(group: String, name: String) extends Creature;

def born(creature: Creature) = creature match {
  case Fish(name) => println("fish:" + name)
  case Animal(group, name) => println(group + ":" + name)
}

born(Fish("koi")) // fish:koi
born(Animal("dog", "wolf")) //dog: wolf
```
