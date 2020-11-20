import random

def median(j):
    route = j[0]
    Left, Right = 0, len(j) - 1
    while Left != Right:
        while Right != Left and j[Right] > route:
            Right -= 1
        j[Left], j[Right] = j[Right], j[Left]
        while Left != Right and j[Left] <= route:
            Left += 1
        j[Left], j[Right] = j[Right], j[Left]
    return Left

def Smallest_element(j, t):
    index = random.randrange(len(j))
    j[0], j[index] = j[index], j[0]
    
    pos = median(j)
    if pos == t - 1:
        return j[pos]
    elif pos < t - 1:
        return Smallest_element(j[pos + 1:], t - pos - 1)
    else:
        return Smallest_element(j[:pos], t)

def main():
    n = int(input())
    j = list(map(int, input().split()))
    t = int(input())
    print(Smallest_element(j, t))

if __name__ == '__main__':
    main()
