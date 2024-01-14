from itertools import tee, islice

## Get the frequency of any n-gram
def ngrams(lst, n):
  tlst = lst
  while True:
    a, b = tee(tlst)
    l = tuple(islice(a, n))
    if len(l) == n:
      yield l
      next(b)
      tlst = b
    else:
      break


import re
from collections import Counter
words = re.findall('\w+', open("PridePrejudice.txt").read())
Counter(ngrams(words, 2)))
