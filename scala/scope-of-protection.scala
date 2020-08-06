class Person(){
  private val name = "hoge"
  private[this] val nickname = "chicken"
  def greet = {
    println(this.name)
    println(this.nickname)
    
    val p = new Person
    println(p.name)
    // println(p.nickname) Error
  }
}
(new Person).greet
