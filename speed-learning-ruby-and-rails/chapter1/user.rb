class User 
   attr_accessor :name, :address
  def initialize(name, address)
    @name = name
    @address = address
  end
end

user = User.new("taro", "tokyo")
print("#{user.name}は#{user.address}に住んでいる")