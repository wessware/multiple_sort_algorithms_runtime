
n = int(input('Enter size of the list: \n'))


def create_a_list(a):
    mylist = [46, 23, 47, 56, 76, 23, 23]
    a = mylist
    
    for i in range(0,n):
        temp = int(input('Enter the number to append: \n'))
        mylist.append(temp)
        
    return a
def three_way_merge_sort(a):
    if len(a) == 1:
        return a
    
    if len(a) == 2:
        h = len(a)
        b = [a[0]]
        m = [a[1]]
        c = []
    else:
        h = len(a)
        h_1 = n // 3
        h_2 = n // 2
        
        l = a[0:h_1]
        m = a[h_1:h_2+1]
        r = a[h_2+1:h]
        
        three_way_merge_sort(l)
        three_way_merge_sort(m)
        three_way_merge_sort(r)
        
        k = 0 
        p = 0
        j = 0
        for i in range(n):
            if k < len(l) and p < len(m)  and j < len(r):
                x  = l[k]
                z = m[p]
                y = r[j]
                
                if x < y and x < z:
                    a[i] = x
                    k += 1
                elif y < x and y < z:
                    a[i] = y
                    j += 1
                elif z < y and z < x:
                    a[i] = z
                    p += 1
                elif y == x or y == z:
                    a[i] = y 
                    j += 1
                elif x == z:
                    a[i] = x
                    k += 1
            elif k == len(l):
                if p < len(m) and j < len(r):
                    z = m[p]
                    y = r[j]
                    
                    if z < y:
                        a[i] = z
                        p += 1
                    elif y < z:
                        a[i] = y
                        j += 1
                    elif z == y:
                        a[i] = y
                        j += 1
                elif p == len(m):
                    while j < len(r):
                        a[i] = r[j]
                        j += 1
                        i += 1
                elif j == len(r):
                    while p < len(m):
                        a[i] = r[j]
                        j += 1
                        i += 1
            elif p == len(m):
                if k < len(l) and j < len(r):
                    x = l[k]
                    y = r[j]
                    
                    if x < y:
                        a[i] = x
                        k += 1
                    elif y < x:
                        a[i] = y 
                        j += 1
                elif k == len(l):
                    while j < len(r):
                        a[i] = r[j]
                        j += 1
                        i += 1
                elif j == len(r):
                    while k < len(l):
                        a[i] = l[k]
                        k +=  1
                        i += 1
                elif j == len(r):
                    if k < len(l) and p < len(m):
                        x = l[k]
                        z = m[p]
                        
                        if x < z:
                            a[i] = x
                            k += 1
                        elif z < x:
                            a[i] = z
                            p += 1
                        elif x == z:
                            a[i] = z
                            p += 1
                elif k == len(l):
                    while p < len(m):
                        a[i] = m[p]
                        p += 1
                        i += 1
                elif k == len(m):
                    a[i] = l[k]
                    k += 1
                    i += 1
    return a
a = create_a_list([])
print(three_way_merge_sort(a))
                        
                    