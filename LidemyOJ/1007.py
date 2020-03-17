# https://oj.lidemy.com/problem/1007

def main():
    x = int(input())
    arr = []
    for i in range(x):
        inp = input().split()
        arr.append((inp[0], int(inp[1])))
    arr.sort(key = lambda x: x[1], reverse = True)
    highestScore = arr[0][1]
    print(arr[0][0])
    for i in range(1, x):
        if arr[i][1] == highestScore:
            print(arr[i][0])
        else:
            break

if __name__ == "__main__":
    main()
