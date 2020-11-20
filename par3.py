def code(j, index1, index2):
    j[index1], j[index2] = j[index2], j[index1]

def par3(j):
    route = j[0]
    LeftLess, Left, Right, RightGreater = 0, 0, len(j) - 1, len(j) - 1
    while Left <= Right:
        while Left <= Right and j[Left] <= route:
            if j[Left] < route:
                code(j, LeftLess, Left)
                LeftLess += 1
            Left += 1
        code(j, Left, Right)
        while Left <= Right and j[Right] >= route:
            if j[Right] > route:
                code(j, Right, RightGreater)
                RightGreater -= 1
            Right -= 1
        code(j, Left, Right)

def main():
    n = int(input())
    j = list(map(int, input().split()))
    par3(j)
    print(' '.join(map(str, j)))

if __name__ == '__main__':
    main()
