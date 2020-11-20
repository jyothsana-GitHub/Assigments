def find(a, i):
    lower, upper = 0, len(a) - 1
    while lower <= upper:
        middle = (lower + upper) // 2
        if a[middle] == i:
            return middle + 1
        elif a[middle] < i:
            lower = middle + 1
        else:
            upper = middle - 1
    return -1

def main():
    n = int(input())
    m = int(input())
    a = list(map(int, input().split()))
    print(' '.join([str(find(a, i)) for i in map(int, input().split())]))

if __name__ == '__main__':
    main()
