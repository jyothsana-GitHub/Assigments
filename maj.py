def majority(a, code):
    return len(list(filter(lambda x: x == code, a))) * 2 > len(a)

def findmajority(a):
    code, count = None, 0
    for number in a:
        if count == 0:
            code, count = number, 1
        elif number == code:
            count += 1
        else:
            count -= 1
    return code if majority(a, code) else -1

def main():
    k, n = map(int, input().split())
    print(' '.join(str(findmajority(list(map(int, input().split())))) for _ in range(k)))

if __name__ == '__main__':
    main()
