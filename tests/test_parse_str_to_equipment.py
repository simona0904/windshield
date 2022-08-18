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
        eurocode = "7251ACDVW1M"
        result = parse_str_to_equipment(eurocode)
        self.assertEqual(result, (False, False, False))

    def test_eurocode_with_sensor_and_1M(self): 
        eurocode = "7251ACDMVW1M"
        result = parse_str_to_equipment(eurocode)
        self.assertEqual(result, (True, False, False)) 

    def test_eurocode_with_camera(self):
        eurocode = "7301AGACVZ"
        result = parse_str_to_equipment(eurocode)
        self.assertEqual(result, (False, True, False))    

    def test_eurocode_without_camera_and_1C(self): 
        eurocode = "3743AGNV1C"
        result = parse_str_to_equipment(eurocode)
        self.assertEqual(result, (False, False, False))

    def test_eurocode_with_camera_and_1C(self): 
        eurocode = "7294AGNCWZ1C"
        result = parse_str_to_equipment(eurocode)
        self.assertEqual(result, (False, True, False))  

    def test_eurocode_with_sensor_camera_heat(self):
        eurocode = "7300AGACHIMVZ75"
        result = parse_str_to_equipment(eurocode)
        self.assertEqual(result, (True, True, True))

    def test_eurocode_with_sensor_camera(self):
        eurocode = "7300AGACIMVZ75"
        result = parse_str_to_equipment(eurocode)
        self.assertEqual(result, (True, True, False))

    def test_eurocode_with_sensor_heat(self):
        eurocode = "7300AGAIHMVZ75"
        result = parse_str_to_equipment(eurocode)
        self.assertEqual(result, (True, False, True))    
           
       

            


