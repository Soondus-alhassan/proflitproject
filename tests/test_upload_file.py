from unittest import TestCase, main
from upload_file import split


class TestUploadFile(TestCase):

    def test_split(self):
        expected = '.xlsx'
        result = split(file='Book1.xlxs')
        self.assertEqual(expected,result)



    


        
        
    
    
   
