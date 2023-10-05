import os

def split(file):
 split_tup = os.path.splitext(file)
 return split_tup[1]

