import Domain.{User, UserName, UserID}
import Service.UserService

object Repository extends App{
  trait Repository{
    var userRepository: List[User]
    def save(user: User): Unit
    def find(key: UserID): Boolean
  }

  class UserRepository extends Repository(){
    var userRepository: List[User] = List()

    def save(user: User): Unit = {
      userRepository ::= user
      userRepository.foreach(it => println(it.toString))
    }

    def find(key: UserID): Boolean = {
      return userRepository.exists(it => it.userID == key)
    }

    def debug(name: String): Option[User] = {
      val found: Option[User] = userRepository.find(it => it.userName.value == name)
      return found match{
        case Some(it) => Some(it.copy())
        case None => None
      }
    }
  }
}
