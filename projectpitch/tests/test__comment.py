import unittest
from app.models import News

class commentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
       

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comments,comments))