#!/usr/bin/ruby

require_relative 'int_is_prime'

module IntFactorize
  def factorize
    arr = []
    number = self
    if number < 2
      raise "#{number} is not prime factorizable."
    end
    while not number.is_prime?
      (2..(number/2).floor).each do |i|
        if number % i == 0
          number /= i
          arr.push i
          break
        end
      end
    end
    arr.push number
    arr
  end
end

class Integer
  prepend IntFactorize
end

