from unittest import TestCase
from minimummachineoperators import machineoperators
import unittest



class MinimumMachineOperators(TestCase):
    def test_generate_sequence_1(self):
        sequence = machineoperators([15,10],12,5)
        self.assertEqual(sequence, 3)

    def test_generate_sequence_2(self):
        sequence = machineoperators([11,15,13],9,5)
        self.assertEqual(sequence, 7)

    def test_generate_sequence_3(self):
        sequence = machineoperators([61,10],50,5)
        self.assertEqual(sequence, 5)

    def test_generate_sequence_4(self):
        sequence = machineoperators([40,10],10,5)
        self.assertEqual(sequence, 8)


    def test_generate_sequence_with_emptylst_5(self):
        sequence = machineoperators([],12,5)
        self.assertEqual(sequence, "The machines list is empty")

    def test_generate_sequence_with_float_value_machine_6(self):
        sequence = machineoperators([15.1,10],12,5)
        self.assertEqual(sequence, 'Not an integer values, please give integer values')


    def test_generate_sequence_with_float_so_7(self):
        self.assertRaises(TypeError, machineoperators,[15,10], 12.1,1)

    def test_generate_sequence_with_float_mo_8(self):
        self.assertRaises(TypeError, machineoperators,[15,10], 12,1.5)

    def test_generate_sequence_with_so_range_exceed_9(self):
        sequence = machineoperators([15,10],1000,1000)
        self.assertEqual(sequence, "Does not satisfy the constraint, please provide proper range value")


    def test_generate_sequence_with_mo_range_exceed_10(self):
        sequence = machineoperators([15,10],999,1001)
        self.assertEqual(sequence, "Does not satisfy the constraint, please provide proper range value")

    def test_generate_sequence_with_machine_range_exceed_11(self):
        sequence = machineoperators([15,101],12,5)
        self.assertEqual(sequence, "Does not satisfy the constraint, please provide proper range value")
    def test_generate_sequence_with_so_range_below_12(self):
        sequence = machineoperators([15,10],0,1000)
        self.assertEqual(sequence, "Does not satisfy the constraint, please provide proper range value")

    def test_generate_sequence_with_mo_range_below_13(self):
        sequence = machineoperators([15,10],999,0)
        self.assertEqual(sequence, "Does not satisfy the constraint, please provide proper range value")

    def test_generate_sequence_with_machine_range_below_14(self):
        sequence = machineoperators([15,0],12,5)
        self.assertEqual(sequence, "Does not satisfy the constraint, please provide proper range value")


if __name__ == '__main__':
    unittest.main()



