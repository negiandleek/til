class Cat
  def chease(mouse)
    puts "chase #{mouse}"
  end
end

tama = Cat.new
tama.chease("test")

executed = "use unless" unless false
print(executed)

print({"japan": 123, "usa": 321});
print({:japan => 123, :usa => 321});
print({japan: 123, usa: 321});

print(obj ||= 10)
obj = nil
print(obj&.name)
arr = %w(apple, banana, orange)
p(arr)
arr2 = %i(apple, banana, orange)
p(arr)

class User
  attr_accessor :name
end

user1 = User.new
user1.name = "hoge"
user2 = User.new
user2.name = "fuga"
user3 = User.new
user3.name = "piyo"

users = [user1, user2, user3]
names = []
users.each do |user|
  names << user.name
end
p names

names2 = []
for user in users
  names2 << user.name
end
p names2

names3 = users.map {|user| user.name}
p names3

users = [user1, user2, user3]
names4 = users.map(&:name)
p names3