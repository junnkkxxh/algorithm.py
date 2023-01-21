n = int(input())

antenna_positions = list(map(int, input().split()))

antenna_positions.sort()

print(antenna_positions[(n-1)//2])