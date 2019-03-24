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
