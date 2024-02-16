import unittest
from my_package import OperatorTrie, find_cheapest_operator


class TestRouting(unittest.TestCase):
    def setUp(self):
        # Setup common to all tests (initializing operators)
        self.operator_a = OperatorTrie('Operator A')
        self.operator_b = OperatorTrie('Operator B')

        # Setup Operator A
        self.operator_a.insert('1', 0.9)
        self.operator_a.insert('268', 5.1)
        self.operator_a.insert('46', 0.17)

        # Setup Operator B
        self.operator_b.insert('1', 0.92)
        self.operator_b.insert('44', 0.5)
        self.operator_b.insert('467', 1.0)

    def test_exact_match(self):
        # Test for exact match
        operators = [self.operator_a, self.operator_b]
        number = '1'
        cheapest_operator, cheapest_price = find_cheapest_operator(
            number, operators)
        self.assertEqual(cheapest_operator, 'Operator A')
        self.assertEqual(cheapest_price, 0.9)

    def test_no_match(self):
        # Test for number with no match
        operators = [self.operator_a, self.operator_b]
        number = '999'
        cheapest_operator, cheapest_price = find_cheapest_operator(
            number, operators)
        self.assertIsNone(cheapest_operator)
        self.assertIsNone(cheapest_price)

    def test_partial_match(self):
        # Assuming the setup makes Operator A cheaper for "467123"
        operators = [self.operator_a, self.operator_b]
        number = '467123'
        cheapest_operator, cheapest_price = find_cheapest_operator(
            number, operators)
        # Expecting Operator A as the cheapest
        self.assertEqual(cheapest_operator, 'Operator A')
        # Ensure the price matches the expected rate
        self.assertAlmostEqual(cheapest_price, 0.17)

    def test_longest_match(self):
        # Test to ensure the longest prefix match is used
        self.operator_a.insert('4673', 0.5)
        operators = [self.operator_a, self.operator_b]
        number = '4673123'
        cheapest_operator, cheapest_price = find_cheapest_operator(
            number, operators)
        self.assertEqual(cheapest_operator, 'Operator A')
        self.assertEqual(cheapest_price, 0.5)


if __name__ == '__main__':
    unittest.main()
