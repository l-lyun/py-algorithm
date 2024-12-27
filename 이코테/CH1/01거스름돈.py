
'''
문제 링크: 이코테 그리디 거스름돈
카테고리: 그리디
문제 해설: 동전 거스름돈 갯수

for coin in coin_types
파이썬에서 array를 충분히 활용할 수 있다.

(옵션)참조링크:
'''

import sys 


def main():
    N = int(sys.stdin.readline().rstrip())

    coin_types = [500, 100, 50, 10]
    cnt = 0

    for coin in coin_types:
        cnt += int(N // coin)
        N %= coin
        
    print(cnt)
        
main()