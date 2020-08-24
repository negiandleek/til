import scala.util.matching.Regex

object Value extends App {

  case class Name(value: String) {
    if (value.isEmpty() == true) {
      throw new IllegalArgumentException("一文字以上入力する必要があります")
    }
    if (value.matches("^[a-zA-Z]+$") == false) {
      throw new IllegalArgumentException("無効な文字列")
    }
  }

  case class FullName(fistName: Name, lastName: Name)

  case class Money(amount: Float, currency: String){
    def add(money: Money): Money = {
      if(currency != money.currency){
        throw new IllegalArgumentException(s"通過単位が異なります")
      }
      return Money(amount + money.amount, currency)
    }
  }

  case class UserName(value: String)
  case class UserId(){
    val value = "test"
  }
  case class User(name: String){
    var userName = UserName(name)
    var userId = UserId()
  }
  def createUser(name: String): Unit = {
    var user = User(name)
//    誤った代入を防ぐ
//    user.userId = "aaa"
  }
}
