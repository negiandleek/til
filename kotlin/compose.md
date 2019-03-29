```kotlin
fun main(args: Array<String>) {
	class Dog(val name: String){
		private var distance: Int = 0;
        fun run(): Int{
            distance += 10;
            return distance;
        }
        fun back():Int{
            distance = 0;
            return distance;
        }
        fun getDistance():Int = distance;
    }
    
   	fun compose(dog:Dog, count: Int, call: (Dog) -> Boolean): Boolean{
       	for(i in 1..count){
            dog.run()
        }
        val r = call(dog);
		println(r);
        return r;
    }
    
    fun callback(dog: Dog): Boolean{
        if(dog.getDistance() <= 20){
            return true
        }else{
            return false
        }
    }
    
    val pet = Dog("pochi");
    compose(pet, 2, ::callback);
    compose(pet, 4, {it -> callback(it)});
}
```
