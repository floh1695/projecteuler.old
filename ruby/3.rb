#!/usr/bin/ruby

require_relative 'func/prime_tools'

answer = PrimeFactorSet.new(600851475143).largest_prime
puts "3\t: #{answer}"

