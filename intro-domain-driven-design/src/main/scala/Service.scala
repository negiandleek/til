import Domain.User
import Repository.UserRepository

object Service extends App {
  class UserService(userRepository: UserRepository){
    def exists(user: User): Boolean = {
      return userRepository.find(user.userID)
    }
  }
}

