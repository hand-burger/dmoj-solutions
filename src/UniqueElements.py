n = int(input())

arr = [int(input()) for i in range(n)]

# Use a set because it means it's all unique

print(len(set(arr)))
