import Domain.{User, UserName}
import Service.UserService

object Repository extends App{
  class UserRepository(){
    var userRepository: List[User] = List()

    def createUser(name: String, key: String) = {
      val user = User(UserName(name), key)
      val userService = new UserService(userRepository)
      if(userService.exists(user)){
        throw new Error("ユーザーは存在しています")
      }else{
        save(user)
      }
    }

    def save(user: User) = {
      userRepository ::= user
      userRepository.foreach(it => println(it.toString))
    }
  }
}
