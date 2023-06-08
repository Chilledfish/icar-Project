import unittest

from testbed import sit
from model_nomalizer import normalize_datagov_models


class TestSitting(unittest.TestCase):
	def test_sit(self):
		self.assertEqual(sit('4+7'), 11)
		self.assertEqual(sit(8), 8)
	def test_values(self):
		self.assertRaises(ValueError, sit, 'k+4')





a = 'moo'