import unittest
from windshield.utils import parse_str_to_equipment


class ParseStrToEquipment(unittest.TestCase):

    def test_eurocode_without_equipment(self):
        eurocode = "2036AGSBL"
        result = parse_str_to_equipment(eurocode)
        self.assertEqual(result, (False, False, False))

    def test_eurocode_with_sensor(self):
        eurocode = "2434AGNGNMV"
        result = parse_str_to_equipment(eurocode)
        self.assertEqual(result, (True, False, False))

    def test_eurocode_without_sensor_and_1M(self): 
        eurocode = "7251ACDVW1M00"
        result = parse_str_to_equipment(eurocode)
        self.assertEqual(result, (False, False, False))

    def test_eurocode_with_sensor_and_1M(self): 
        eurocode = "7251ACDMVW1M00"
        result = parse_str_to_equipment(eurocode)
        self.assertEqual(result, (True, False, False))    


