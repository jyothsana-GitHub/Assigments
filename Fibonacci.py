def main():
    n = int(input())
    prev = 1
    fibo = 0
    for _ in range(n):
        prev, fibo = fibo, prev + fibo
    print(fibo)

if __name__ == '__main__':
    main()
