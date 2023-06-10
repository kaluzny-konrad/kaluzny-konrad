# to run write in terminal: python script.py data.txt 6

import argparse
import os
import datetime


def get_data_from_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read().split('\n')
        return data


def get_table_from_data(data, num_of_columns):
    table = []
    for i in range(0, len(data), num_of_columns):
        table.append(data[i:i+num_of_columns])
    return table


def remove_empty_rows(table):
    table_without_empty_rows = []
    for row in table:
        if row[0] != '':
            table_without_empty_rows.append(row)
    return table_without_empty_rows


def save_table_to_csv(table, filename, delimiter=';'):
    try:
        now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        filepath = f'{filename}_{now}.csv'
        with open(filepath, 'w', encoding='utf-8') as f:
            for row in table:
                for i in range(0, len(row)):
                    f.write(f'{row[i]}')
                    if (i < len(row) - 1):
                        f.write(delimiter)
                f.write('\n')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file_path', type=str)
    parser.add_argument('num_of_columns', type=int)
    args = parser.parse_args()

    data = get_data_from_file(args.data_file_path)
    table = get_table_from_data(data, args.num_of_columns)
    clean_table = remove_empty_rows(table)
    save_table_to_csv(clean_table, 'table')
