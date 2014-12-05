#!//usr/busr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import progressbar
from time import sleep
"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  ret=[]
  url=re.findall(r'GET.+jpg',open(filename,'rU').read())
  for x in url:
  	ret.append('http://code.google.com'+x[4:])
  return ret

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  bar=progressbar.ProgressBar(maxval=len(img_urls),widgets=[progressbar.Bar('=','[',']'),' ',progressbar.Percentage()])
  i=0
  for x in img_urls:
     try:
	bar.update(i+1)
	urllib.urlretrieve(x,dest_dir+'/'+x.split('/')[-1])
	sleep(0.1)
     except IOError:
	print '*'
  bar.finish()
  
def main():
  args = sys.argv[1:]
  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)
  
  todir = sys.argv[2]

  img_urls = read_urls(args[0])
  if not os.path.exists(todir):
    os.mkdir(todir)
  if os.path.isdir(todir):
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
