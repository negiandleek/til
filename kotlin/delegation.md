# Property Delegation
```kotlin
interface HogeFuga{
    fun call(): Unit;
}


fun main(args: Array<String>) {
	class Hoge(): HogeFuga{
        override fun call(): Unit = println("Hoge");
    }
    
    class Fuga(b: Hoge): HogeFuga by b;
    
    val hoge = Hoge();
    Fuga(hoge).call();
}
```
# Observable
```kotlin
import kotlin.properties.Delegates

fun main(args: Array<String>) {
	class Hoge{
        var p: String by Delegates.observable("<no name>"){
            prop, old, new -> 
            	println("$old -> $new");
        }
    }
    
    val hoge = Hoge()
    hoge.p = "a";
    hoge.p = "b";
}
```
