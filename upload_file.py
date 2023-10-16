''' 
'upload_file' in app.py carries out multiple tasks

1. checks the form if file has been uploaded
--- can be replaced with try/except

2. loads the requested file onto 'file'

3. checks if the filename is empty or just a space

4. saves a file path

5. redirects to process route
'''

import os
from hello import secure_filename


def sanitize(upload):
  return secure_filename(upload)

def split(upload):
 ''' splits filename and checks for .xlxs file extension'''
 return os.path.splitext(upload)

def check_extension(upload):
    ''' splits filename and checks for .xlxs file extension'''
    result = split(upload)
    return result[1] 

def name_of_upload(upload):
  result = split(upload)
  return result[0]

def join(filename):
  '''create new filename for sanitized excel file'''
  return 'sanitized_'+ filename

def lower_case(filename):
  return filename.lower()

