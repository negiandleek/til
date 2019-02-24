```scala
trait Edge{
  def a: String;
  def b: String;
};
case class ExtendEdge(a: String, b:String, right:Int, asked:Int ) extends Edge;

val edgeQa = ExtendEdge("hoge", "fuga", 1, 2);

abstract class Test(val hoge: String, val piyo:String= "piyo");
abstract class Test2{
  val fuga: String;
  val piyo: String = "piyo"
}
abstract class Test3;

class ExtendTest(hoge: String) extends Test(hoge);
class ExtendTest2(val fuga: String) extends Test2;
class ExtendTest3(bar: String) extends Test3;

val hoge = new ExtendTest("hoge");
println(hoge.hoge, hoge.piyo);
val fuga = new ExtendTest2("fuga");
println(fuga.fuga, fuga.piyo);
val bar = new ExtendTest3("bar");
// println(bar.bar) //error

trait TestValOrDef{
  val valValue: Any;
  def defValue: Any;
}

class ExtendTestValOrDef(a: String, b: String) extends TestValOrDef{
  val valValue = a;
  val defValue = b
}
class ExtendTestValOrDefError() extends TestValOrDef{
  def valValue: Unit = println("a"); //error
  def defValue: Unit = println("b");
}
new ExtendTestValOrDef("a", "b");
```
