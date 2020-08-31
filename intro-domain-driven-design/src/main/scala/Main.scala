import Domain.{User, UserName}
import Repository.UserRepository
import Service.UserService

object Main extends App{
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
