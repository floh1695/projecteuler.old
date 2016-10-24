#!/usr/bin/ruby

require_relative 'func/prime_tools'

#=====================================================================
# ** Problem 10
#---------------------------------------------------------------------
#  * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#  * Find the sum of all the primes below two million.
#=====================================================================
def main
  answer = 0
  (1..2000000).each do |prime_candidate|
    if prime_candidate.is_prime?
      answer += prime_candidate
    end
  end
  puts "10\t: #{answer}"
end

main

