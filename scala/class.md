# use Abstract
```scala
abstract class Pet(val animal: String){
  val name: String;
  val roar: String;
  def cry(): Unit;
}

class Cat(val name: String, val roar: String = "meow") extends Pet("cat"){
  private var _count: Int = 0;
  def count = _count;
  override def cry(): Unit = {
    increment();
    println(name + "(" + animal + ") cry '"  + roar.toUpperCase() + "'");
  }
  
  def increment(): Int = {
    _count += 1;
    _count;
  }
}

val cat = new Cat("tama");
cat.cry();
println(cat.count)

class Kitten(name: String, roar: String = "mie") extends Cat(name, roar){
  override def cry(): Unit =
    increment();
    println(name + "(" + animal + "-baby) cry '"  + roar + "'");
}

val kitten = new Kitten("pochi");
kitten.cry();
println(kitten.count)
```
# use Trait
```scala
trait Pet{
  val name: String;
  val roar: String;
  private var count: Int = 0;
  def cry(): Unit = println(name + " cry " +roar);
  def increment(): Int = {
    count += 1;
    count;
  }
}

class Cat(val name: String, val roar: String = "meow") extends Pet{}

val cat = new Cat("cat");
cat.cry();
println(cat.increment())

class Kitten(name: String, override val roar: String = "mie") extends Cat(name, roar){
  override def cry(): Unit = println(name + " cry " + roar);
}

val kitten = new Kitten("kitten", "mie");
kitten.cry()
```

# mixin
```scala
abstract class Animal{
  val name: String;
}

trait Pet{
  val nickname: String;
}

class Dog(val name: String, val nickname: String) extends Animal with Pet

class Golden(name: String, nickname: String) extends Dog(name, nickname);

val dog = new Dog("dog", "pochi");

println(dog.name,  dog.nickname);
```

## コンパイルエラー
```scala
  class A
  class B
  class C extends A with B
```
