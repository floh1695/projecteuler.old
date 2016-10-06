#!/usr/bin/ruby

answer = 0
1000.times do |i|
  if i % 3 == 0 or i % 5 == 0
    answer += i
  end
end

puts "1\t: #{answer}"

