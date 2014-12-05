#/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
def print_words(x):
	dic={}
	x=open(x).read().split()
	for x1 in x:
		dic.setdefault(x1,0)
		if x1 in dic:
			dic[x1]=dic.get(x1,0)+1
	for dic1 in sorted(dic.items(),key=lambda x:x[1],reverse=True):
		print dic1[0],dic1[1]
def print_top(x):
	dic={}
        x=open(x).read().split()
        for x1 in x:
                dic.setdefault(x1,0)
                if x1 in dic:
                        dic[x1]=dic.get(x1,0)+1
	i=0
        for dic1 in sorted(dic.items(),key=lambda x:x[1],reverse=True):
	     if i<=20:
                print dic1[0],dic1[1]
	     i+=1
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
