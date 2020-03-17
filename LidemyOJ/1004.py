# https://oj.lidemy.com/problem/1004

def main():
    x = int(input())
    for i in range(x):
        inp = input().split()
        a = int(inp[0])
        b = int(inp[1])
        rule = int(inp[2])
        if rule == 1:
            if a > b:
                print("A")
            elif a == b:
                print("DRAW")
            else: 
                print("B")
        else:
            if a > b:
                print("B")
            elif a == b:
                print("DRAW")
            else: 
                print("A")

if __name__ == "__main__":
    main()
