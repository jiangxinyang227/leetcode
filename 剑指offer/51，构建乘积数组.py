"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。
"""


def multiply(a):
    if not a:
        return []
    b = [1] * len(a)

    front_temp = 1
    for i in range(1, len(a)):
        front_temp *= a[i - 1]
        b[i] *= front_temp

    back_temp = 1
    for j in range(len(a) - 1, 0, -1):
        back_temp *= a[j]
        b[j - 1] *= back_temp

    return b


array = [1, 2, 3, 4, 5]
res = multiply(array)
print(res)
