from unittest import TestCase
from upload_file import split,join


class TestUploadFile(TestCase):

    def test_split(self):
        expected = '.xlxs'
        result = split(filename='Book1.xlxs')
        self.assertEqual(expected,result)


    def test_join(self):
        result = join(filename='Book1')
        expected = 'sanitized_Book1'
        self.assertEqual(expected, result)


    


        
        
    
    
   
