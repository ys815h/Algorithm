def solution(n):
    x = int(n**(1/2))
    if n == x*x:
      return (x+1)*(x+1)
    return -1