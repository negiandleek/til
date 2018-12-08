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
