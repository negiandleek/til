# 宣言側変性(Declaration-site variant)
```kotlin
interface BarBaz<out T>{
    fun get(): T;
}

interface HogeFuga<in T>{
	fun set(item: T): MutableList<Any>;
}

fun main(args: Array<String>) {
    class Bar(var value: List<String>): BarBaz<String>{
        override fun get(): String{
            return value[0];
        }
    }
    
    println(Bar(listOf("a", "b")).get())
    
    class Hoge(var value: MutableList<Any>): HogeFuga<String>{
        override fun set(item: String): MutableList<Any>{
            value.add(item);
            return value;
        }
    }
    
    println(Hoge(mutableListOf("a","b","c")).set("d"));
}
```

# 型投影(type projection)
```kotlin
interface Animal<out T, in U>{
    val list: List<T>;
    fun get(index: Int): T;
    fun set(value: U): T;
}

fun main(args: Array<String>) {
    class Dog(val name: String);
    
    class Dogs(override var list: List<Dog>): Animal<Dog, String>{
       	override fun get(index: Int): Dog{
            return list[index];
        }
        override fun set(value: String): Dog{
            val dog = Dog(value);
            list = list + listOf(dog);
            return dog;
        }
    }
    
    val dogs = listOf(Dog("pochi"), Dog("hachi"));
    val dogPets = Dogs(dogs);
    dogPets.set("taro");
    println(dogPets.get(2));
}
```
