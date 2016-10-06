#!/usr/bin/ruby

module IntegerExtIsPrime
  def is_prime?
    if self < 2
        return false
    end
    (2..(self/2).floor).each do |i|
      if self % i == 0
        return false
      end
    end
    true
  end

  def is_composite?
    if [0, 1].include? self
      return false
    end
    not is_prime?
  end
end

class Integer
  prepend IntegerExtIsPrime
end

