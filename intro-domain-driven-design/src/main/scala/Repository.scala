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
  }

  class Program(){
    var repository = new UserRepository()

    def createUser(name: String, key: String) = {
      val user = User(UserName(name), key)
      val userService = new UserService(repository)
      if(userService.exists(user)){
        throw new Error("ユーザーは存在しています")
      }else{
        repository.save(user)
      }
    }
  }
}
