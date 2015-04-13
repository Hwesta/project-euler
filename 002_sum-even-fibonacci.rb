#!/usr/bin/env ruby

# Done 2015-04-22
def first_try(max_value)
    max_value
end

if __FILE__ == $0
    max = ARGV[0].to_i
    puts "max value is #{max}"
    puts first_try max
end