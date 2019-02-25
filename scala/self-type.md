```scala
trait User{
  val name: String;
}

trait Tweeter{
  this: User =>
  def tweet(value: String): Unit = println(s"$name: $value");
}

class VerifiedTweeter(val name: String) extends User with Tweeter;

val tweet = new VerifiedTweeter("Mr");
tweet.tweet("yahoooo!")
```
