#!/usr/bin/ruby

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

