import unittest
from main import add_new_product_to_dict, update_existing_product_in_dict, update_product_brand_data_in_dict, process_one_row


class TestSum(unittest.TestCase):
    def test_add_new_product_to_dict(self):
        """
        Test that it adds the new row to the dict
        """
        dict = {}
        add_new_product_to_dict(dict, 'shoes', 2,'Air')
        added_row = dict.get('shoes')
        added_brand = added_row[1].get('Air')
        self.assertEqual(added_row[0], 2)
        self.assertEqual(added_brand, 1)

    def test_update_product_brand_data_in_dict(self):
        """
        Test that it updates the brand data of an existing product in the dict
        """
        # case1: update existing brand
        dict1 = {'Air': 2, 'BonPied': 2}
        new_brand_data1 = update_product_brand_data_in_dict(dict1, 'BonPied')
        updated_brand = new_brand_data1.get('BonPied')
        self.assertEqual(updated_brand, 3)
        self.assertDictEqual(new_brand_data1, {'Air': 2, 'BonPied': 3})

        # case2: add new brand
        dict2 = {'Air': 2}
        new_brand_data2 = update_product_brand_data_in_dict(dict2, 'BonPied')
        self.assertDictEqual(new_brand_data2, {'Air': 2, 'BonPied': 1})

    def test_update_existing_product_in_dict(self):
        """
        Test that it updates an existing row in the dict
        """
        dict = {'shoes': [15.0, {'Air': 2, 'BonPied': 2}], 'forks': [9.0, {'Pfitzcraft': 1, 'Xcraft': 2}]}
        update_existing_product_in_dict(dict, 'shoes', 3, 'BonPied')
        updated_row = dict.get('shoes')
        updated_brand = updated_row[1].get('BonPied')
        self.assertEqual(updated_row[0], 18.0)
        self.assertEqual(updated_brand, 3)

    def test_process_one_row(self):
        """
        Test that it process onw row and add/update it in the dict
        """
        # case1: process existing product
        dict = {'shoes': [5.0, {'Air': 1}], 'forks': [9.0, {'Pfitzcraft': 1, 'Xcraft': 2}]}
        row = ['D5', 'Minneapolis', 'shoes', '2', 'Air']
        process_one_row(dict, row)
        self.assertDictEqual(dict, {'shoes': [7.0, {'Air': 2}], 'forks': [9.0, {'Pfitzcraft': 1, 'Xcraft': 2}]})

        # case2: add new produc
        dict = {'forks': [9.0, {'Pfitzcraft': 1, 'Xcraft': 2}]}
        row = ['D5', 'Minneapolis', 'shoes', '2', 'Air']
        process_one_row(dict, row)
        self.assertDictEqual(dict, {'shoes': [2.0, {'Air': 1}], 'forks': [9.0, {'Pfitzcraft': 1, 'Xcraft': 2}]})

if __name__ == '__main__':
    unittest.main()