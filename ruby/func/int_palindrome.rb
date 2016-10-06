#!/usr/bin/ruby

module IntPalindrome
  def is_palindromic?
    number = to_s
    size = number.size
    aran = (0)..((size/2) - 1)
    bran = (size - (size/2))..(size)
    aarr = number[aran]
    barr = number[bran]
    aarr == barr.reverse
  end
end

class Integer
  prepend IntPalindrome
end

