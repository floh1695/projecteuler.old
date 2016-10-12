#!/usr/bin/ruby

puzzle_numbers = (1..7)

puzzle_numbers.each do |puzzle_number|
  require_relative puzzle_number.to_s
end

