def length_binary_search(array, target, start, end):

    while start <= end:
        mid = (start+end) // 2
        len_sum = sum([a-mid for a in array if a >= mid])
        if len_sum == target:
            return mid
        elif len_sum > target:
            start = mid + 1
        else:
            end = mid - 1

    return None


n, m = map(int, input().split())
ricecakes = list(map(int, input().split()))

print(length_binary_search(ricecakes, m, 0, max(ricecakes)))
