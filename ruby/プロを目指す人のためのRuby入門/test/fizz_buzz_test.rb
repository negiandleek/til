require 'minitest/autorun'
require_relative '../lib/2_fizz_buzz'

class FizzBuzzTest < Minitest::Test
    def test_fizz_buzz
        assert_equal '11', fizz_buzz(11)
        assert_equal 'Buzz', fizz_buzz(10)
        assert_equal 'Fizz', fizz_buzz(12)
        assert_equal 'FizzBuzz', fizz_buzz(15)
    end
end