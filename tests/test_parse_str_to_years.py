import unittest

from windshield.utils import parse_str_to_years

class TestParseStrToYears(unittest.TestCase):

    def test_for_start_year_after_2000(self):
        value = '.00/01-05/09'   
        result = parse_str_to_years(value)
        self.assertEqual(result, (2000, 2005))

    def test_for_start_year_before_2000(self):
        value = '.98/01-08/09' 
        result = parse_str_to_years(value)
        self.assertEqual(result, (1998, 2008))

    def test_for_end_year_before_2000(self):
        value = '.89/01-98/09' 
        result = parse_str_to_years(value)
        self.assertEqual(result, (1989, 1998))

    def test_for_no_end_year(self):
        value = '.89/01-'
        result = parse_str_to_years(value)
        self.assertEqual(result, (1989, None))

    def test_for_empty_string_value(self):
        value = ""
        with self.assertRaises(ValueError):
            result = parse_str_to_years(value)

    def test_for_invalid_str_value(self):
        value = 'abcdefghijkl'
        with self.assertRaises(ValueError):
            result = parse_str_to_years(value)

    

        








