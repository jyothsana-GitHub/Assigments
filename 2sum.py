def sum(t):
    test = {}
    for i in range(len(t)):
        if -t[i] in test:
            return test[-t[i]], i
        test[t[i]] = i
    return None

def main():
    m, n = map(int, input().split())
    for _ in range(m):
        indices = sum(list(map(int, input().split())))
        if indices:
            print(indices[0] + 1, indices[1] + 1)
        else:
            print(-1)

if __name__ == '__main__':
     main()
