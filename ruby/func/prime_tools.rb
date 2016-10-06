#!/usr/bin/ruby

require_relative 'int_is_prime'
require_relative 'int_factorize'

class PrimeFactorSet
  def initialize number
    @number = number
    @prime_factors = number.factorize
  end

  def largest_prime
    @prime_factors.max
  end

  def smallest_prime
    @prime_factor.min
  end
end

