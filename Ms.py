n = input()
arr = [int(a) for a in input().split()]

arr.sort()

print (' '.join([str(a) for a in arr]))
