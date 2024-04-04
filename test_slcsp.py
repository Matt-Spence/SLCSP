import unittest
import pandas as pd
from slcsp import *

class TestSLCSPScript(unittest.TestCase):
    def test_find_slcsp_rate_one_plan(self):
        # Test case where there's only one silver plan in a rate area
        rate_area_plans = pd.read_csv('test_data/test_plans_only_1.csv')
        self.assertIsNone(find_slcsp_rate(rate_area_plans))

    def test_find_slcsp_rate_two_plans(self):
        # Test case where there are 2 silver plans in a rate area
        rate_area_plans = pd.read_csv('test_data/test_plans_only_2.csv')
        self.assertEqual(find_slcsp_rate(rate_area_plans), 625.0)

    def test_find_slcsp_rate_same_rate(self):
        # Test case where all silver plans have the same rate in a rate area
        rate_area_plans = pd.read_csv('test_data/test_plans_all_silver_same.csv')
        self.assertIsNone(find_slcsp_rate(rate_area_plans))

    def test_find_slcsp_rate_multiple_metals(self):
        # Test case where there are multiple silver and non-silver plans in a rate area
        rate_area_plans = pd.read_csv('test_data/test_AK_RA1.csv')
        self.assertEqual(find_slcsp_rate(rate_area_plans), 597.0)

    def test_process_zip_codes_single_zip_code(self):
        # Test case where single ZIP code belongs to a single rate area
        zips_df = pd.read_csv('test_data/test_zips_1.csv')
        plans_df = pd.read_csv('test_data/test_plans_1.csv')
        expected_output_df = pd.DataFrame.from_dict({'zipcode': [1], 'rate': [587.0]})
        expected_output_df = expected_output_df.astype({"rate": object})    # processed_df will contain objects instead of float64's. I spent way too much time on this error.
        processed_df = process_zip_codes(zips_df, plans_df, pd.DataFrame.from_dict({'zipcode': [1], 'rate': ['']}))        
        self.assertTrue(processed_df.equals(expected_output_df))

    def test_process_zip_codes_multiple_zip_codes(self):
        # Test case where multiple ZIP codes belong to single rate areas
        zips_df = pd.read_csv('test_data/test_zips_2.csv')
        plans_df = pd.read_csv('test_data/test_plans_2.csv')
        expected_output_df = pd.DataFrame.from_dict({'zipcode': [1, 2], 'rate': [590.0, 495.0]})
        expected_output_df = expected_output_df.astype({"rate": object})    # processed_df will contain objects instead of float64's. I spent way too much time on this error.
        processed_df = process_zip_codes(zips_df, plans_df, pd.DataFrame.from_dict({'zipcode': [1, 2], 'rate': ['', '']}))
        self.assertTrue(processed_df.equals(expected_output_df))

    def test_process_zip_codes_multiple_rate_area(self):
        # Test case for ZIP code belonging to multiple rate areas
        zips_df = pd.read_csv('test_data/test_zips_2.csv')
        plans_df = pd.read_csv('test_data/test_plans_2.csv')
        expected_output_df = pd.DataFrame.from_dict({'zipcode': [3], 'rate': ['']})
        processed_df = process_zip_codes(zips_df, plans_df, pd.DataFrame.from_dict({'zipcode': [3], 'rate': ['']}))
        self.assertTrue(processed_df.equals(expected_output_df))

    def test_process_zip_codes_no_rate_area(self):
        # Test case for ZIP code belonging to no rate areas
        zips_df = pd.read_csv('test_data/test_zips_1.csv')
        plans_df = pd.read_csv('test_data/test_plans_1.csv')
        expected_output_df = pd.DataFrame.from_dict({'zipcode': [2], 'rate': ['']})
        processed_df = process_zip_codes(zips_df, plans_df, pd.DataFrame.from_dict({'zipcode': [2], 'rate': ['']}))
        self.assertTrue(processed_df.equals(expected_output_df))

if __name__ == '__main__':
    unittest.main()
