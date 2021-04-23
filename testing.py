lst=[[1,2,3],[0,3,4]]
add=0
new_lst=list()
new_str=""
for i in range(len(lst)-1):
    for j in range(len(lst)+1):
        if(lst[i+1][j]==0):
            
        add=(lst[i][j]/lst[i+1][j])
        new_lst.append(str(int(add))+'x^'+str(len(lst)+1-j))
new_str="+".join(new_lst)
print(new_str)

