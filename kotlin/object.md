```kotlin
open class XY(val x: Int, val y: Int);
val xy = object: XY(10, 20){
    fun add(): Int{
        return x + y;
    }
};
println(xy.add());
```
