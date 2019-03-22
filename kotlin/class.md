```kotlin
interface Pet {
  val name: String;
  fun call(name: String){
      println("come on!! " + name);
  }
};

fun main(){
  open class Animal(val name: String){
        open fun call() {
            print(name);
        }
    }

    class Dog : Animal, Pet{
        constructor(name: String): super(name);
        override fun call(){
			println("hi " + name);
        	super<Pet>.call(name);
        }
    }
    
    val pochi = Dog("pochi");
    pochi.call();
}
```
