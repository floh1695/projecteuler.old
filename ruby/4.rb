#!/usr/bin/ruby

require_relative 'func/int_palindrome'

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

