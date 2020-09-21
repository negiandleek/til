class Person
  def initialize(money: 0)
    @money = money
  end
  def billionaire?()
    money >= 100000000
  end
  private
  def money 
    @money
  end
end

taro = Person.new(money: 1000000000)
print(taro.billionaire?)