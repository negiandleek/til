object Value extends App {
  case class FirstName(value: String){
    if(value.isEmpty() == true){
      throw new IllegalArgumentException("error")
    }
  }
  case class LastName(value: String){
    if(value.isEmpty() == true){
      throw new IllegalArgumentException("error")
    }
  }
  case class FullName(fistName: FirstName, lastName: LastName)
}
