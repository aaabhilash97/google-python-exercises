#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import progressbar
from time import sleep
"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

# LAB(begin solution)
def get_special_paths(dirname):
  """Given a dirname, returns a list of all its special files."""
  result = []
  paths = os.listdir(dirname) # list of paths in that dir
  for fname in paths:
      result.append(os.path.abspath(os.path.join(dirname, fname)))
  return result


def copy_to(paths, to_dir):
  """Copy all of the given files to the given dir, creating it if necessary."""
  if not os.path.exists(to_dir):
    os.mkdir(to_dir)
  bar=progressbar.ProgressBar(maxval=len(paths),widgets=[progressbar.Bar('=','[',']'),' ',progressbar.Percentage()])
  i=0
  for path in paths:
    fname = os.path.basename(path)
    if os.path.isfile(os.path.join(to_dir, fname)):
	    shutil.copy(path, os.path.join(to_dir, fname))
    bar.update(i+1)
    sleep(00.1)
  bar.finish()

def zip_to(paths,zipfile):
	cmd="zip -j "+ zipfile+" "+' '.join(paths)
	(status,output)=commands.getstatusoutput(cmd)
	if status:
		sys.stderr.write(output)
		sys.exit()
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)
  paths=get_special_paths(args[2])
  if args[0]=="--todir":
	copy_to(paths,args[1])
  elif args[0]=="--tozip":
	zip_to(paths,args[1])
if __name__ == "__main__":
	main()
