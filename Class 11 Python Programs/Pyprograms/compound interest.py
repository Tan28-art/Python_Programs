if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

for i in arr:
    max_of_arr = max(arr)
    li = []
    if i<max_of_arr:
        li.append(i)
print(max(li))

