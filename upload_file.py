import os


def split(filename):
 ''' splits filename and checks for .xlxs file extension'''
 split_tup = os.path.splitext(filename)
 return split_tup[1]


def join(filename):
  '''create new filename for sanitized excel file'''
  return 'sanitized_'+ filename




