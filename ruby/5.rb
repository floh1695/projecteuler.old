#!/usr/bin/ruby

require_relative 'func/prime_tools'

def find_factors ran
  factors = []
  ran.each do |i|
    factors += i.factorize
  end
  factors.uniq
end

def add_until arr, ele, count
  while arr.count(ele) < count
    arr.push(ele)
  end
end

def solve primes, ran
  solved_for = []
  ran.each do |i|
    ifactors = i.factorize
    ifactors.uniq.each do |j|
      add_until solved_for, j, ifactors.count(j)
    end
  end
  solved_for
end

answer = 1
ran = 2..20
factors = find_factors ran
solved_factors = solve factors, ran
puts solved_factors
answer = solved_factors.reduce :*

puts "5\t: #{answer}"

