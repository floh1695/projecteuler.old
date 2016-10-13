#!/usr/bin/ruby

require_relative 'func/int_palindrome'

#=====================================================================
# ** Problem 4
#---------------------------------------------------------------------
#  * A palindromic number reads the same both ways. The largest
#    palindrome made from the product of two 2-digit numbers is:
#    
#      9009 = 91 × 99.
#
#  * Find the largest palindrome made from the product of two 3-digit
#    numbers.
#=====================================================================
def main
  answer = 0
  num = 999
  (100..num).each do |a|
    (a..num).each do |b|
      product = a * b
      if product.is_palindromic?
        if product <= answer
          break
        else
          answer = product
        end
      end
    end
  end

  puts "4\t: #{answer}"
end

main

