pp nil.to_s
pp 1.to_s
pp true.to_s
pp "---"
pp 1.to_s
pp 1.to_s()
pp "---"
x = {'japan' => 'yen', 'us' => 'dollar'}
pp x
pp "---"
x,y = 100, 200, 300
pp x, y
z, zz = 400, 500,600
pp(z, zz)
pp "---"
pp "a\nb"
pp 'a\nb'
pp "---"
a = [1,2,3]
b = {'hoge' => 'ほげ', 'fuga' => 'ふが'}
pp a
puts a
pp b
puts b
pp "a\nb"
puts "a\nb"
a = b = 'value'
a.upcase!
pp a,b
pp "---"
pp 1 / 3
pp 1.0 / 3.0
pp "---"
pp 1 + '2'.to_i
pp 1.to_s + '2'
pp (0.1r * 3r).to_f
pp "---"
country = 'hoge'
country_local = 
    if country == 'hoge'
        'ほげ国'
    elsif country == 'fuga'
        'ふが国'
    else
        'ぴよ国'
    end
pp country_local
pp "---"
point = 2
day = 3
point *= 5 if day == 3
pp point
pp "ポイントは #{point} です"
pp "---"
pp %$hoge,fuga,piyo$
pp %!hoge,fuga,piyo!
puts <<TEXT
hoge
fuga
piyo
TEXT
pp "---"
pp 0b1111
pp 0o10
pp 0x10
pp 2e3
pp 2e-3
country = 'japan'
pp case country
when 'japan'
    'こんにちは'
when 'spain'
    'ciao'
else
    'hello'
end
pp '---'
def greet(suffix = '!') = "hello#{suffix}"
pp greet('??')
pp "---"
def increment(n) 
    n = n + 1
    pp n
end
n = 10
increment(10)
pp n
pp "---"
require 'date'
pp Date.today
require_relative './2_fizz_buzz'
pp fizz_buzz(45)