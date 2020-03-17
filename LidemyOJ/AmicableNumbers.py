# https://oj.lidemy.com/problem/1005

import math

def factorsSum(num):
    arr = []
    factors = 0
    for i in range(1, int(math.sqrt(num) ) + 1):
        if num % i == 0:
            factors += i
            arr.append(i)
            if num // i != i and num // i != num:
                factors += num // i
                arr.append(num // i)
#    print(arr)
    return factors

def main():
    x = int(input())
    while x!= 0:
        amicable = factorsSum(x)
        if factorsSum(amicable) == x:
            print(amicable)
        else:
            print("QQ")
        x = int(input())

if __name__ == "__main__":
    main()
