import unittest
from fibonacci_lattice import FibonacciLattice

class FibonacciLatticeTestCase(unittest.TestCase):
    def setUp(self):
        self.lattice = FibonacciLattice(3, 3)

    def tearDown(self):
        self.lattice = None

    def test_valid_label(self):
        self.assertTrue(self.lattice.is_valid([1, 4, 7]))
        self.assertTrue(self.lattice.is_valid([2, 4, 7]))
        self.assertTrue(self.lattice.is_valid([2, 4, 8]))
        self.assertTrue(self.lattice.is_valid([3, 5, 8]))

        self.assertFalse(self.lattice.is_valid([3, 4, 8]))
        self.assertFalse(self.lattice.is_valid([3, 6, 7]))
        self.assertFalse(self.lattice.is_valid([3, 6, 10]))
        self.assertFalse(self.lattice.is_valid([-1, 4, 7]))

    def test_size(self):
        self.assertEqual(len(self.lattice.nodes()), 21)
        self.assertEqual(len(self.lattice.edges()), 38)
