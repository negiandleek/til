[VARIANCES](https://docs.scala-lang.org/tour/variances.html)

# copy
```scala
//Convariance
abstract class Animal{
  val name: String
}
case class Cat(val name: String) extends Animal;
case class Dog(val name: String) extends Animal;

object CovarianceTest extends App {
  def printAnimalNames(animals: List[Animal]): Unit = {
    animals.foreach(animal => println(animal.name));
  }
}

val cats: List[Cat] = List(Cat("Whiskers"), Cat("Tom"));
val dogs: List[Dog] = List(Dog("Fido"), Dog("Rex"));
CovarianceTest.printAnimalNames(cats);
CovarianceTest.printAnimalNames(dogs);

//Contravariance
abstract class Printer[-A]{
  def print(value: A): Unit;
};

class AnimalPrinter extends Printer[Animal]{
  def print(animal: Animal): Unit = 
    println("The animal's name is" + animal.name);
};

class CatPrinter extends Printer[Cat]{
  def print(cat: Cat): Unit = 
    println("The cat's name is" + cat.name);
};

object ContravariantceTest extends App {
  def printMyCat(printer: Printer[Cat], myPet: Cat): Unit = 
    printer.print(myPet);
}

val catPrinter: Printer[Cat] = new CatPrinter;
val animalPrinter: Printer[Animal] = new AnimalPrinter;
val myCat: Cat = Cat("Boots");
ContravariantceTest.printMyCat(catPrinter, myCat);
ContravariantceTest.printMyCat(animalPrinter, myCat);

//Invariance
class Container[A](value: A){
  private var _value: A = value;
  def getValue: A = _value
  def setValue(value: A): Unit = {
    _value = value
  }
}

val catContainer: Container[Cat] = new Container(Cat("Felix"));
val animalContainer: Container[Animal] = catContainer; //Error
```
