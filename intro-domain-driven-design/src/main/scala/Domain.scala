import java.util.UUID

object Domain extends App{
  case class UserName(val value: String){
    if(value.isEmpty() == true){
      throw new Error("error")
    }
  }

  case class UserID(val value: String){
    if(value.isEmpty() == true){
      throw new Error("error")
    }
  }

  case class User(userName: UserName, key: String){
//    val userID = UserID(UUID.randomUUID().toString)
    val userID = UserID(key)
    def equals(obj: User): Boolean = obj.userID == userID
  }

//Service
  class UserListService(){
    var userList: List[User] = List()
    def createUser(name: String, key: String) = {
      val existed = userList.exists(it => it.userID == key)
      if(existed == true){
        throw new Error("ユーザーは存在しています")
      }else{
        userList ::= User(UserName(name), key)
      }
    }
  }
}
