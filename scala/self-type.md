```scala
trait User{
  def username: String;
};

trait Bird{
  this: User => 
  def tweet(): Unit = println(username + ":" + "tweettweet");
}

class Exec(val username: String) extends User with Bird

new Exec("hoge").tweet() //hoge:tweettweet
```
