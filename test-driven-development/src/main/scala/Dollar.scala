package money

class Dollar(var amount: Int){
  def times(multiplier: Int): Dollar ={
    amount *= multiplier
    return new Dollar(amount * multiplier)
  }
}