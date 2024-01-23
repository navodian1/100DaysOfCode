def largest(_arr, n):
    max1 = _arr[0]

    for i in range(1, n):
        if _arr[i] > max1:
            max1 = _arr[i]
    return max1


arr = input("enter numbers using comma")
_len = len(arr)
Ans = largest(arr, _len)
print("Largest in given array ", Ans)
