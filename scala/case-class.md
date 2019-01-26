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

# And If
```scala
abstract class Message;
case class Phone(phoneNumber: Int, message: String) extends Message;

def checkImportantMessage(message: Message, subscribed: Seq[Int]): String = {
  message match {
    case Phone(phoneNumber, _) if subscribed.contains(phoneNumber) =>
      "important";
    case other => 
      "other"
  }
}

val subscribed = Seq(12341234);
val test = new Phone(12341234, "Hi!!");
val test2 = new Phone(43214321, "hi??")
println(checkImportantMessage(test, subscribed)); // "important"
println(checkImportantMessage(test2, subscribed)); // "other"
```

# Type Only
```scala
abstract class Phone;

class MobilePhone extends Phone;
class SmartPhone extends Phone;

def newOrOld(p: Phone): String = p match {
  case p: MobilePhone => "old"
  case p: SmartPhone => "new"
}

println(newOrOld(new MobilePhone)) //old
```
