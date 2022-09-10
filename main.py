# This is a problem solving code challenge to precess a csv file with orders data
# and calculate some aggregation data on these orders
# The hashtable (dictionary) is the main data structure used due to its constant time complexity O(1)
# Created by: Khaled Mousa
from csv import reader, writer
import copy


# write the output data from the hashtable into the csv files
# used only one loop for both file lists for better time complexity
def write_output_data_csv_file(file_name, data_dictionary, orders_count):
    avg_rows, pop_brands_rows = [], []
    # looping on all products in the hash table to process
    for product in data_dictionary.keys():
        # Calculate the avg product per order
        total_quantities = data_dictionary.get(product)[0]
        avg = str(total_quantities / orders_count)
        avg_rows.append([product, avg])

        # Calculate the popular (max) brand as max count in the brands nested hashtable
        brands_dict = data_dictionary.get(product)[1]
        popular_brand = max(brands_dict, key=brands_dict.get)
        pop_brands_rows.append([product, popular_brand])
    try:
        # write the avg data in the first csv file
        with open('0_' + file_name, 'wt') as csv_file:
            csv_writer = writer(csv_file)
            csv_writer.writerows(avg_rows)
            csv_file.close()
        # write the popular brands in the second csv file
        with open('1_' + file_name, 'wt') as csv_file:
            csv_writer = writer(csv_file)
            csv_writer.writerows(pop_brands_rows)
            csv_file.close()
    except Exception as e:
        print('an error occured', e)


# Reads row by row from the csv file, add processed data into a hash table (dictionary)
def process_data_from_csv_file(file_name):
    data_dictionary = {}
    orders_count = 0
    try:
        # read the data from the csv file, line by line
        with open(file_name, 'r') as csv_orders:
            rows_reader = reader(csv_orders)
            for row in rows_reader:
                orders_count += 1
                process_one_row(data_dictionary, row)
        write_output_data_csv_file(file_name, data_dictionary, orders_count)
        print(data_dictionary)
    except FileNotFoundError:
        print('file not found')
    except:
        print('an error occured')


# takes one row from the file reader and update the dictionary data
def process_one_row(data_dictionary, row):
    product = row[2]
    quantity = float(row[3])
    brand = row[4]
    if product in data_dictionary:
        update_existing_product_in_dict(data_dictionary, product, quantity, brand)
    else: add_new_product_to_dict(data_dictionary, product, quantity, brand)


# Update the quantity sum and brand data of an existing product in the hash table
def update_existing_product_in_dict(data_dictionary, product, quantity, brand):
    current_product_data = data_dictionary.get(product)
    current_quantity_data = current_product_data[0]
    current_brand_data = current_product_data[1]
    new_quantity_data = current_quantity_data + quantity
    new_brand_data = update_product_brand_data_in_dict(current_brand_data, brand)
    new_product_data = [new_quantity_data, new_brand_data]
    data_dictionary[product] = new_product_data


# Add the product, quantity, and brand data as a new entry in the hash table
def add_new_product_to_dict(data_dictionary, product, quantity, brand):
    data_dictionary[product] = [quantity, {brand: 1}]


# Update the nested hash table of the product brand data with the new data
def update_product_brand_data_in_dict(current_brand_data, brand):
    # It doesn't matter in this case to keep the old brand data or not, but i just copied it
    new_brand_data = copy.deepcopy(current_brand_data)
    # Increase the brand count by 1
    if brand in current_brand_data:
        new_brand_data[brand] = current_brand_data[brand] + 1
    else: new_brand_data[brand] = 1
    return new_brand_data


def start():
    # file_name = input('Enter file name: ')
    file_name = 'orders.csv'
    process_data_from_csv_file(file_name)
    print('Done successfuly, please check the output files in the same directory')


if __name__ == '__main__':
    start()
