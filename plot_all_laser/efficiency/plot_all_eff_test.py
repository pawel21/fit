import numpy as np
import unittest

from plot_all_eff import Data


class DataTest(unittest.TestCase):
    def test_should_return_input_power(self):
        #GIVEN
        fake_data = Data("fake_data.txt")
        #WHEN
        expected_input_power = [1, 4, 16]
        input_power = fake_data.get_input_power()
        #THEN
        self.assertEqual(expected_input_power[0], input_power[0])
        self.assertEqual(expected_input_power[1], input_power[1])
        self.assertEqual(expected_input_power[2], input_power[2])

if __name__ == "__main__":
    unittest.main()