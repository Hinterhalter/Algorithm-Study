lst = [5,8,6,4,9,0,1,2,3,7]

max = -2145000000

for i in range(len(lst)):
    for j in range(len(lst)):
        if i != j:
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

print(lst)