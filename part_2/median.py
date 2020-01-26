import csv
from heapq import heappush, heappop


def load_data(file_path):
    data =[]
    with open(file_path, 'r') as f:
        data_reader = csv.reader(f)
        for row in data_reader:
            for item in row:
                data.append(int(item))

    return data


def median_maintenance(x):
    hlo = []
    hhi = []
    m_i = 0
    m = 0
    sm = 0
    for i in range(0,len(x)):
        if x[i] <= m:
            heappush(hlo, -x[i])
        elif x[i] > m:
            heappush(hhi, x[i])
        if len(hlo) < len(hhi):
            m = heappop(hhi)
            heappush(hlo, -m)
        elif len(hlo) - 1 > len(hhi):
            tmp = -heappop(hlo)
            heappush(hhi, tmp)
            m = -hlo[0]
        sm += m
    return sm, m

if __name__ == '__main__':
    a = load_data('Median.txt')
    med_sum, med = median_maintenance(a)
    print(med_sum)