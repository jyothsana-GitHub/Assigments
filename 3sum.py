def threesum(t):
    two_ind = {}
    for i in range(len(t)):
        if t[i] not in two_ind:
            two_ind[t[i]] = set()
        two_ind[t[i]].add(i)
    
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            target_c = -t[i] - t[j]
            if target_c in two_ind:
                indices = list(filter(lambda x: x != i and x != j, two_ind[target_c]))
                if indices:
                    return i, j, indices[0]

def main():
    k, n = map(int, input().split())
    for _ in range(k):
        indices = threesum(list(map(int, input().split())))
        if indices:
            print(' '.join(map(lambda x: str(x + 1), indices)))
        else:
            print(-1)

if __name__ == '__main__':
    main()
