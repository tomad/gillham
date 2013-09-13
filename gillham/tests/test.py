import unittest
import warnings

import os
import json
from gillham import gillham


class TestGillhamDecode(unittest.TestCase):

    def setUp(self):
        self.set_valid_codes()

    def set_valid_codes(self):
        this_dir = os.path.dirname(__file__)
        gillham_code_path = os.path.join(this_dir, 'fixtures', 'gillham.json')
        gillham_code = file(gillham_code_path, 'r')
        alts = json.load(gillham_code)

        valid_alts = []
        valid_bits = []

        for upper, lower, bits in alts:
            median = int((((upper - lower) / 2) + lower))
            valid_alts.append(median)
            valid_bits.append(bits[2:])

        assert len(valid_alts) == 1278
        assert len(valid_bits) == 1278

        self.valid_alts = valid_alts
        self.valid_bits = valid_bits

    def test_conversion_of_valid_codes(self):
        all_alts = []
        for bits in self.valid_bits:
            code = int('0' + bits, base=2)
            g = gillham(code)
            all_alts.append(g)

        self.assertSequenceEqual(self.valid_alts, all_alts)

    def test_warnings_for_all_invalid_codes(self):

        invalid = []

        for i in range(2 ** 12):
            valid = True

            bit_pattern = '{0:012b}'.format(i)

            with warnings.catch_warnings(record=True) as warns:
                code = int(bit_pattern, base=2)
                converted_alt = gillham(code)

            if converted_alt and converted_alt not in self.valid_alts:
                valid = False

            if bit_pattern not in self.valid_bits:
                if not valid:
                    print("failed alts test {0}".format(converted_alt))
                    print("failed bits test {0}".format(bit_pattern))
                valid = False

            if not valid and not warns:
                invalid.append(converted_alt)
                print("No warning for invalid alt: b:{0} g:{1}".format(
                    bit_pattern,
                    converted_alt)
                )

        self.assertEqual(0, len(invalid))
