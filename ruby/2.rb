#!/usr/bin/ruby

require_relative 'func/fib'

def main
  answer = 0
  fib_n = 0
  while true
    fib_r = fib fib_n
    fib_n += 1
    if fib_r <= 4000000
      if fib_r % 2 == 0
        answer += fib_r
      end
    else
      break
    end
  end
  
  puts "2\t: #{answer}"
end

main

