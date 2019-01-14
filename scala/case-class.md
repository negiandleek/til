```scala
case class Pet(name: String, kind: String, age: Int);
val dog = Pet("pochi", "DOG", 10);
println(dog); //Pet(pochi,DOG,10)
// dog.name = "tama" Error

val dog2 = dog.copy(name = "hachi", age = 2);
println(dog2) //Pet(hachi,DOG,2)
```
