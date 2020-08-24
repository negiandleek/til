import java.util.UUID

object Entity extends App{
  class UserID(){
    val id = UUID.randomUUID().toString
  }
//  TODO
  case class User(private var name: String, val id: UserID = new UserID()){
    if(name.length() < 3){
      throw new IllegalArgumentException("3文字以上")
    }
    def changeName(value: String): Unit = {
      if (value.length() < 3) {
        throw new IllegalArgumentException("3文字以上")
      } else {
        name = value
      }
    }
  }
}