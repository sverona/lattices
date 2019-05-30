import unittest
from fibonacci_lattice import FibonacciLattice

class FibonacciLatticeTestCase(unittest.TestCase):
    def setUp(self):
        self.lattice = FibonacciLattice(3, 3)

    def tearDown(self):
        self.lattice = None

    def test_is_valid_label(self):
        self.assertTrue(self.lattice.is_valid_label((1, 4, 7)))
        self.assertTrue(self.lattice.is_valid_label((2, 4, 7)))
        self.assertTrue(self.lattice.is_valid_label((2, 4, 8)))
        self.assertTrue(self.lattice.is_valid_label((3, 5, 8)))

        self.assertFalse(self.lattice.is_valid_label((3, 4, 8)))
        self.assertFalse(self.lattice.is_valid_label((3, 6, 7)))
        self.assertFalse(self.lattice.is_valid_label((3, 6, 10)))
        self.assertFalse(self.lattice.is_valid_label((-1, 4, 7)))

    def test_size(self):
        self.assertEqual(len(self.lattice.nodes()), 21)
        self.assertEqual(len(self.lattice.edges()), 38)

    def test_is_adjacent(self):
        self.assertTrue(self.lattice.is_adjacent((1, 4, 7), (1, 4, 8)))
        self.assertTrue(self.lattice.is_adjacent((1, 4, 7), (1, 5, 7)))

        self.assertFalse(self.lattice.is_adjacent((1, 4, 7), (1, 5, 8)))

    def test_edge_color(self):
        self.assertEqual(self.lattice.edge_color((1, 4, 7), (1, 4, 8)), 1)
        self.assertEqual(self.lattice.edge_color((1, 4, 7), (1, 5, 7)), 2)

        self.assertIsNone(self.lattice.edge_color((1, 4, 7), (1, 5, 8)))

    def test_vertex_weight(self):
        self.assertEqual(self.lattice.vertex_weight((1, 4, 7)), (2, 1))
        self.assertEqual(self.lattice.vertex_weight((1, 4, 8)), (0, 2))
        self.assertEqual(self.lattice.vertex_weight((1, 5, 7)), (3, -1))

if __name__ == "__main__":
    unittest.main()
