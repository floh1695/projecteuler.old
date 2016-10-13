#!/usr/bin/ruby

require_relative 'func/prime_tools'

#=====================================================================
# ** Problem 7
#---------------------------------------------------------------------
#  * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
#    we can see that the 6th prime is 13.
#
#  * What is the 10001st prime?
#=====================================================================
def main
  answer = 0
  prime_counter = 0
  while true
    answer += 1
    if answer.is_prime?
      prime_counter += 1
      if prime_counter == 10001
        break
      end
    end
  end
  puts "7\t: #{answer}"
end

main

