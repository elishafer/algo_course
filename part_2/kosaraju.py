__author__ = 'Elisei Shafer'

import csv

def load_file(file_path):
    r_data = []
    with open(file_path, 'r') as f:
        data_reader = csv.reader(f, delimiter=' ')
        r_data = [row[:2] for row in data_reader]
    return r_data


if __name__ == '__main__':
    data = load_file('SCC.txt')
    print(data[0])