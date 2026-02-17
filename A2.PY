list1=[10,20,30,40,50]
def cube(n):
    return n*n*n

result=list(map(cube,list1))
print(result)