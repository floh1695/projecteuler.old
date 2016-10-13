#!/usr/bin/ruby

require_relative 'func/prime_tools'

#=====================================================================
# ** Problem 5
#---------------------------------------------------------------------
#  * 2520 is the smallest number that can be divided by each of the
#    numbers from 1 to 10 without any remainder.
#
#  * What is the smallest positive number that is evenly divisible by
#    all of the numbers from 1 to 20?
#=====================================================================
def main
  answer = 1
  ran = 2..20
  factors = find_factors ran
  solved_factors = solve factors, ran
  answer = solved_factors.reduce :*
  
  puts "5\t: #{answer}"
end

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

main

