# https://dmoj.ca/problem/ccc06j2

m = int(input())
n = int(input())
count = 0

for i in range(1, m+1):
    if 10 - i in range(1, n+1):
        count += 1

print("There are " + str(count) + " ways to get the sum 10.") if count != 1 else print(
    "There is " + str(count) + " way to get the sum 10.")
