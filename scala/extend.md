```scala
class Hoge(val name: String);
class Fuga(_name: String){
  val name = _name;
}
abstract class Bar{
  def name: String;
}
class Baz(val name: String) extends Bar;

val hoge = new Hoge("hoge");
val fuga = new Fuga("fuga");
val bar = new Baz("bar");
println(hoge.name, fuga.name, bar.name);

class PiyoHoge(name: String) extends Hoge(name);
class PiyoFuga(name: String) extends Fuga(name);
class PiyoBaz(name: String) extends Baz(name);

val piyoHoge = new PiyoHoge("hoge");
val piyoFuga = new PiyoFuga("fuga");
val piyoBaz = new PiyoBaz("baz");

println(piyoHoge.name, piyoFuga.name, piyoBaz.name);
```
