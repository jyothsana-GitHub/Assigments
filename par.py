def par(t):
    route = t[0]
    Left, Right = 0, len(t) - 1
    while Left != Right:
        while Right != Left and t[Right] > route:
            Right -= 1
        t[Left], t[Right] = t[Right], t[Left]
        while Left != Right and t[Left] <= route:
            Left += 1
        t[Left], t[Right] = t[Right], t[Left]

def main():
    n = int(input())
    t = list(map(int, input().split()))
    par(t)
    print(' '.join(map(str, t)))

if __name__ == '__main__':
    main()
