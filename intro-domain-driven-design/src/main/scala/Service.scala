import Domain.User
import Repository.UserRepository

object Service extends App {
  class UserService(userRepository: List[User]){
    def exists(user: User): Boolean ={
      return userRepository.exists(it => it.userID == user.userID)
    }
  }
}
