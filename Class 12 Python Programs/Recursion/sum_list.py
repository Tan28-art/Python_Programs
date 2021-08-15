# To find sum of numeric list using recursion
l = eval(input("List: "))
x = len(l)

def sum_list(li, ln):
    if ln == 0:
        return 0
    else:
        return li[ln-1] + sum_list(li,ln-1)

print(sum_list(l,x))