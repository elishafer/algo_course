__author__ = 'Elisei Shafer'


def karatsuba(n1, n2):

    if n1 or n2 < 10:
        return int(n1)* int(n2)

    n1 = str(n1)
    n2 = str(n2)
    m = min(len(n1), len(n2))
    m2 = m >> 1
    a = int(n1[0:-m2])
    b = int(n1[-m2:len(n1)])
    c = int(n2[0:-m2])
    d = int(n2[-m2:len(n2)])

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a+b, c+d) - ac -bd

    return ac * 10 ** m + ad_bc * 10 ** (m >> 1) + bd


if __name__ == '__main__':
    a = karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627)
    print(a)