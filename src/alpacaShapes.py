# https://dmoj.ca/problem/aac1p1

numbers = list(map(int, input().split()))

print('SQUARE') if numbers[0] * numbers[0] > 3.14 * \
    (numbers[1] * numbers[1]) else print('CIRCLE')
