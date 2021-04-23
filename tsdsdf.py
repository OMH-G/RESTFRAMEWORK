lst=[1, 2 ,3, 4, 3, 3, 2, 1]
new_lst=list()
_min=0
while(lst!=[]):
    new_lst.append(len(lst))
    _min=min(lst)
    lst=[i for i in lst if i != min(lst)]
    for i in range(len(lst)):
        lst[i]= lst[i]-_min
print(new_lst)