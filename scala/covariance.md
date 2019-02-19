```scala
abstract class Food{
  def name: String;
};
class Washoku(val name:String) extends Food;
class Sushi(name: String) extends Washoku(name);
class Italy(val name: String) extends Food;

class Menu[+T](val menu: List[T]){
  def order(): Unit = {
    menu.foreach {it  =>
      println(it)
    }
  }
}

val japan = List(new Washoku("Udon"), new Sushi("Toro"));
val japanMenu = new Menu[Washoku](japan);
japanMenu.order();
```
