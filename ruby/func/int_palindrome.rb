#!/usr/bin/ruby

module IntPalindrome
  def is_palindromic?
    to_s == to_s.reverse
  end
end

class Integer
  prepend IntPalindrome
end

