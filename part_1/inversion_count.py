__author__ = 'Elisei Shafer'

import csv

def merge_sort_count(a, n):

    if n == 1:
        return a, 0

    n2 = int(n/2)
    b, x = merge_sort_count(a[:n2],n2)
    c, y = merge_sort_count(a[n2:],n-n2)

    i = j = 0
    d = [None] * n
    z = 0

    for k in range(n):
        if b[i] < c[j]:
            d[k] = b[i]
            i += 1
            if i >= len(b):
                break
        else:
            d[k] = c[j]
            j += 1
            z += len(b) - i # number of values left to go through in array b
            if j >= len(c):
                break

    while i < len(b):
        # finish copying array
        d[len(c)+i] = b[i]
        i += 1

    while j < len(c):
        # finish copying array
        d[len(b)+j] = c[j]
        j += 1

    count = x + y + z

    return d, count

def load_data(file_path):
    data =[]
    with open(file_path, 'r') as f:
        data_reader = csv.reader(f)
        for row in data_reader:
            for item in row:
                data.append(int(item))

    return data


if __name__ == '__main__':
    # a = [1, 3, 5, 2, 4, 6]
    # b = [3, 2, 1, 0]
    # d, count = merge_sort_count(b, 4)
    #
    # print(d)
    # print(count)

    file_path = "inversion_IntegerArray.txt"
    data = load_data(file_path)
    print(len(data))
    print(data[:10])

    d, count = merge_sort_count(data, len(data))
    print(count)
    print(d[:10])
    print(d[-10:])
    print(d[50000:50010])