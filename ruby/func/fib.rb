#!/usr/bin/ruby

def fib n
  a = 0
  b = 1
  n.times do
    o = b
    b = a + b
    a = o
  end
  a
end

