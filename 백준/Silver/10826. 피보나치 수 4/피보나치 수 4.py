# 10826 피보나치 수 4
import sys
input = sys.stdin.readline

n = int(input().strip())

a = 0
b = 1
for i in range(n):
    temp = a + b
    a = b
    b = temp
print(a)