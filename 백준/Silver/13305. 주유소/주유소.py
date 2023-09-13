# 13305 주유소 (실버3)

import sys
input = sys.stdin.readline

# 도시개수
N = int(input().strip())

# 도로의 길이가 제일 왼쪽 도로부터 N-1개의 자연수로 주어진다.
road = list(map(int, input().strip().split()))
city = list(map(int, input().strip().split()))

price = city[0] * sum(road)
temproad = road[0]
totalroad = sum(road)
nowcity = city[0]

for i in range(1, N-1):
    # 가장 저렴한 도시만 체크 하면 된다.
    if nowcity > city[i]:
        price = nowcity * temproad + city[i] * (totalroad - temproad)
        nowcity = city[i]

    temproad += road[i]
print(price)