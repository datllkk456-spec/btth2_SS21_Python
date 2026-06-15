import unittest

from pos_logic import (
    calculate_total,
    add_to_order,
    current_order
)


class TestHighlandsPOS(unittest.TestCase):

    def setUp(self):
        current_order.clear()

        current_order.append({
            "code": "P1",
            "quantity": 2
        })

        current_order.append({
            "code": "F1",
            "quantity": 1
        })

    def test_calculate_total(self):
        result = calculate_total()
        self.assertEqual(result, 125000)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            add_to_order("P1", -5)


if __name__ == "__main__":
    unittest.main()