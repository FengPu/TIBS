import unittest
import sys
sys.path.append('../')
from tibs.pos import posdata

class TestPosData(unittest.TestCase):

    def setUp(self):
        self.posData = posdata.PosData('name', 'id', 'description', 'acc')
    def test_accountiability(self):
    	pass

if __name__ == '__main__':
	unittest.main()