student=["simran","ojasvi","akshita","varnika"]
roll=[1,2,3,4]

dict={s:r for s,r in zip(student[::-1],roll[::-1])}
print(dict)