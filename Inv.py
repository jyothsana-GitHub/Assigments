def cntinversion(a):
    def attach(a, b):
        nonlocal inversion_num
        
        c = []
        inda, indb = 0, 0
        while inda < len(a) or indb < len(b):
            if inda < len(a) and (indb == len(b) or a[inda] <= b[indb]):
                c.append(a[inda])
                inda += 1
            else:
                c.append(b[indb])
                indb += 1
                inversion_num += len(a) - inda
        return c
    
    def attach_sort(a):
        size = len(a)
        if size < 2:
            return a
        return attach(attach_sort(a[:size // 2]), attach_sort(a[size // 2:]))
    
    inversion_num = 0
    attach_sort(a)
    return inversion_num

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(cntinversion(a))

if __name__ == '__main__':
    main()
