# https://oj.lidemy.com/problem/1006

def main():
    x = int(input())
    table = {}
    for i in range(1, x + 1):
        table[i] = True
    y = int(input())
    for i in range(y):
        table[int(input())] = False
    res = 0
    for i in range(1, x + 1):
        if i + 2 <= x:
            if table[i] and i % 2 == 1 and table[i + 1]:
                res += 1
            if table[i] and i % 2 == 1 and table[i + 2]:
                res += 1
            if table[i] and i % 2 == 0 and table[i + 2]:
                res += 1
        elif i + 1 == x:
            if table[i] and table[i + 1]:
                res += 1
            
    print(res)

if __name__ == "__main__":
    main()
