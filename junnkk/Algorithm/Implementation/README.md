## 구현 
: **머릿 속에 있는 알고리즘을 소스코드로 바꾸는 과정**

> 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
> 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
> 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
> 적절한 라이브러리를 찾아서 사용해야 하는 문제

#### 완전 탐색 
: 모든 경우의 수를 주저 없이 다 계산하는 해결 방법


#### 시뮬레이션 
: 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야 하는 문제 유형



<br>

- 일반적으로 알고리즘 문제에서의 2차원 공간은 행렬(Matrix)의 의미로 사용된다.

    
``` python
for i in range(5):
	for j in range(5):
    	print('(',i,',',j,')', end=' ')
    print()
```

<br>

- 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용된다.

    
``` python
# 동, 북, 서, 남
dx = [0,-1,0,1]
dy = [1,0,-1,0]

# 현재 위치
x,y = 2,2

for i in range(4):
	# 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)
```
--> 이코테 책의 상하좌우 문제에서는 dx, dy 를 설정하여 문제를 해결하였다. 
반면, 왕실의 나이트에서는 갈 수 있는 8가지의 방향을 steps = [(-2,-1),...] 과 같이 설정하여 문제를 해결하였다. 