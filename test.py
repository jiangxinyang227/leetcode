def func(n, m):

    left = 1
    right = n
    sum = 0
    while left < right:
        if (left // m) % 2 == 0:
            sum -= left
        else:
            sum += left

        if (right // m) % 2 == 0:
            sum -= right
        else:
            sum += right
        left += 1
        right -= 1
    return sum


res = func(8, 2)
print(res)