#!/usr/bin/ruby

#=====================================================================
# ** Problem 1
#---------------------------------------------------------------------
#  * If we list all the natural numbers below 10 that are multiples of
#    3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#  * Find the sum of all the multiples of 3 or 5 below 1000.
#=====================================================================
def main
  answer = 0
  1000.times do |i|
    if i % 3 == 0 or i % 5 == 0
      answer += i
    end
  end
  
  puts "1\t: #{answer}"
end

main

