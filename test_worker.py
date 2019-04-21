import unittest

from worker import Employee

class TestEmployeeWorker(unittest.TestCase):

    def setUp(self):
        first = 'adam'
        last = 'miseris'
        self.my_moneys = Employee(first, last)
        self.responses = ['500', '800', '300']
    
    def test_store_single_response(self):
        self.my_moneys.give_raise(self.responses[0])
        self.assertIn(self.responses[0], self.my_moneys.responses)
    
    def test_store_three_response(self):
        for response in self.responses:
            self.my_moneys.give_raise(response)
        for response in self.responses:
            self.assertIn(response, self.my_moneys.responses)

unittest.main()