def fizz_buzz(value)
    if value % 15 == 0
        'FizzBuzz'
    elsif value % 3 == 0
        'Fizz'
    elsif value % 5 == 0
        'Buzz'
    else
        value.to_s
    end
end
# pp fizz_buzz(10)
# pp fizz_buzz(24)
# pp fizz_buzz(15)
# pp fizz_buzz(32)
        