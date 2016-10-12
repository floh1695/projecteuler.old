#!/usr/bin/ruby

require_relative 'func/prime_tools'

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

