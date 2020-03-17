# https://oj.lidemy.com/problem/1003

def main():
    x = int(input())
    string = ""
    ans = ""
    for i in range(x):
        string += input()
#    print(string)
    x = int(input())
    for i in range(x):
        ans += string[int(input()) - 1]
    print(ans)

if __name__ == "__main__":
    main()
