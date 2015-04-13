#!/usr/bin/env ruby

require 'set'

# Done 2015-04-22
def first_try(max)
    multiple_3 = Set.new 0.step(max-1, 3).to_a
    multiple_5 = Set.new 0.step(max-1, 5).to_a
    multiples = multiple_3 | multiple_5
    sum = multiples.reduce(:+)
end

if __FILE__ == $0
    max = ARGV[0].to_i
    puts "max is #{max}"
    puts first_try max
end