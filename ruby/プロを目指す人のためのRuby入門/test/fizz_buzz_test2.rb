require 'rspec'
require_relative '../lib/2_fizz_buzz'

RSpec.describe 'FizzBuzz' do
  context 'fizzbuzz' do
    expect(1).to eq 1
    expect(fizz_buzz(10)).to eq 'Buzz'
    expect(fizz_buzz(12)).to eq 'Fizz'
    expect(fizz_buzz(15)).to eq 'FizzBuzz'
  end 
end