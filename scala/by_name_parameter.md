```scala
def echo[A](test: Boolean, whenTrue: => A, whenFalse: => A): A = {
  if(test){
    whenTrue
  }else{
    whenFalse
  }
} 

echo(true, println("success"), println("failure"));
```
