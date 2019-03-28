```kotlin
class Hoge(){
    fun fuga(){
        println("method")
    }
    fun piyo(){
        println("method piyo")
    }
}
fun Hoge.fuga(){ 
    println("extension")
}
fun Hoge.piyo(value: String){
  println("extension piyo");
}
Hoge().fuga() // method
Hoge().piyo() // method piyo
Hoge().piyo("a") // extension piyo
```
