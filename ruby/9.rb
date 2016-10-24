#!/usr/bin/ruby

#=====================================================================
# ** Problem 9
#---------------------------------------------------------------------
#  * A Pythagorean triplet is a set of three natural
#    numbers, a < b < c, for which,
#
#      a**2 + b**2 = c**2
#
#  * For example, 3**2 + 4**2 = 9 +16 = 25 = 5**2
#
#  * There exists exactly one Pythagorean triplet for
#    which a + b + c = 1000.
#
#  * Find the product abc.
#=====================================================================
def main
  answer = find_triplet
 puts "9\t: #{answer}"
end

def find_triplet
  (1..1000).each do |c|
    (1..(c - 1)).each do |b|
      (1..(b - 1)).each do |a|
        if a*a + b*b == c*c
          if a + b + c == 1000
            return a*b*c
          end
        end
      end
    end
  end
end

main

