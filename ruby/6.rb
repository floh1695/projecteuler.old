#!/usr/bin/ruby

#=====================================================================
# ** Problem 6
#---------------------------------------------------------------------
#  * The sum of the squares of the first ten natural numbers is,
#
#      1**2 + 2**2 + ... + 10**2 = 385
#
#  * The square of the sum of the first ten natural numbers is,
#
#      (1 + 2 + ... + 10)**2 = 3025
#
#  * Hence the difference between the sum of the squares of the first
#    ten natural numbers and the square of the sum is,
#
#      3025 − 385 = 2640.
#
#  * Find the difference between the sum of the squares of the first
#    one hundred natural numbers and the square of the sum.
#=====================================================================
def main
  ran = 1..100
  answer = square_of_sums(ran) - sum_of_squares(ran)
  puts "6\t: #{answer}"
end

def sum_of_squares ran
  sum = 0
  ran.each do |i|
    sum += i**2
  end
  sum
end

def square_of_sums ran
  sum = 0
  ran.each do |i|
    sum += i
  end
  sum**2
end

main

