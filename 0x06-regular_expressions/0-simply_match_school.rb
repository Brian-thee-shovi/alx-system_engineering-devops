#!/usr/bin/env ruby
#regular expression which matches school
my_regex = /\bSchool\b/
my_text = ARGV[0]
matches = my_text.scan(my_regex)
puts matches.join
