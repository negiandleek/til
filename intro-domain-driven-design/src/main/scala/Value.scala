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
}
