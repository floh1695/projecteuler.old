#!/usr/bin/ruby

#=====================================================================
# ** Using this for its modular exponentiation.
#---------------------------------------------------------------------
#  * TODO: Implement this.
#=====================================================================
require 'openssl'

module IntegerExtIsPrime
  #===================================================================
  # ** Primality checker
  #-------------------------------------------------------------------
  #  * This is based upon the Fermat primality test,
  #
  #      https://en.wikipedia.org/wiki/Fermat_primality_test
  #===================================================================
  def is_prime?
    if self < 2
      return false
    elsif [2, 3].include? self
      return true
    end
    if 2.to_bn.mod_exp(self - 1, self) == 1
      return self.is_prime_check?
    else
      return false
    end
  end

  def is_prime_check?
    if self < 2
        return false
    end
    (2..(self/2).floor).each do |i|
      if self % i == 0
        return false
      end
    end
    true
  end

  def is_composite?
    if [0, 1].include? self
      return false
    end
    not is_prime?
  end
end

class Integer
  prepend IntegerExtIsPrime
end

