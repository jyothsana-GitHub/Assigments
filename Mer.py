def numread():
    _ = input()
    return list(map(int, input().split()))

def attach(a, b):
    c = []
    inda, indb = 0, 0
    while inda < len(a) or indb < len(b):
        if inda < len(a) and (indb == len(b) or a[inda] <= b[indb]):
            c.append(a[inda])
            inda += 1
        else:
            c.append(b[indb])
            indb += 1
    return c

def main():
    print(' '.join(map(str, attach(numread(), numread()))))

if __name__ == '__main__':
    main()
