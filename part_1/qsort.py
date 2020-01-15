import csv
# from statistics import median

def qsort(a, lo, hi):
    comparisons = 0
    if lo >= hi:
        return 0

    p_i = partition(a, lo, hi)
    comparisons += qsort(a, lo, p_i - 1)
    comparisons += qsort(a, p_i + 1, hi)
    comparisons += hi - lo
    return comparisons


def choose_pivot(a, lo, hi, pivot_type='last'):
    if pivot_type == 'first':
        pass
    elif pivot_type == 'last':
        a[lo], a[hi] = a[hi], a[lo]
    elif pivot_type == 'median':
        mid = int(lo + (hi - lo) / 2)
        med = median(a, lo, mid, hi)
        a[lo], a[med] = a[med], a[lo]
    return lo

def median(a, lo, mid, hi):
    b = a[lo]
    c = a[mid]
    d = a[hi]
    if d > b:
        if d < c:
            median_i = hi
        elif b > c:
            median_i = lo
        else:
            median_i = mid
    else:
        if d > c:
            median_i = hi
        elif b < c:
            median_i = lo
        else:
            median_i = mid

    return median_i


def partition(a, lo, hi):
    p_i = choose_pivot(a, lo, hi)
    p = a[p_i]
    i = lo + 1
    for j in range(lo + 1, hi + 1):
        if a[j] <= p:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[lo], a[i-1] = a[i-1], a[lo]
    return i - 1

def load_data(file_path):
    data =[]
    with open(file_path, 'r') as f:
        data_reader = csv.reader(f)
        for row in data_reader:
            for item in row:
                data.append(int(item))

    return data


if __name__ == '__main__':
    a = load_data('/home/elisei/PycharmProjects/algo_course/part_1/QuickSort.txt')
    comps = qsort(a, 0, len(a) - 1)
    print(comps, a)
    # a = [0, 5, 9, 2, 8, 0, 8, 4, 8, 5, 4]
    # comps = qsort(a, 0, 10)
    # print(comps, a)