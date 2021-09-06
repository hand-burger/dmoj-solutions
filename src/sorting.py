# https://dmoj.ca/problem/a4b1

n = int(input())

arr = [int(input()) for i in range(n)]

arr.sort()

for i in arr:
    print(i)
