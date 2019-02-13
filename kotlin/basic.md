```kotlin
fun main(args: Array<String>) {
  fun maxOf(a: Int, b: Int):Int = if(a > b) a else b;
    val r = maxOf(10, 12);
    println(r);
    
    fun testNull(str: String): String? {
		if(str == "a") return "str";
        else return null;
    };
    println(testNull("a"));
    
    fun getStrLen(obj: Any): Int? {
        if(obj !is String) return null;
        return obj.length;
    };
    println(getStrLen("abc"));
    println(getStrLen(123));
    
    val arr = listOf(10,20,30);
    for(index in arr){
        println(index);
    };
    
    var count = 0;
    while(count < arr.size){
		println(arr[count]);
        count += 1;
    };
    
    fun describe(obj: Any): String{
    	when(obj){
            1 -> return "Number"
            obj is String -> return "String"
            else -> return "Other"
        }
    }
    
    println(describe(1));
    
    for(i in 1..5){
        println(i);
    }
}
```
