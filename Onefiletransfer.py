# with open("file1.","r") as f:
#     f.read()
# with open("file2.txt","w") as g:
#     g.write(f.read())
with open("file1.txt") as f:
    val=f.readline()
b=open("file2.txt","r+")
c=b.write(val)
print(b.read())
b.close()