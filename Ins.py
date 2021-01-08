def InsertionSort(a):
    swap_numb = 0
    for i in range(1, len(a)):
        k = i
        while k > 0 and a[k] < a[k - 1]:
            a[k - 1], a[k] = a[k], a[k - 1]
            swap_numb += 1
            k -= 1
    return swap_numb

def main():
    n = int(input())
    print(InsertionSort(list(map(int, input().split()))))

if __name__ == '__main__':
    main()
