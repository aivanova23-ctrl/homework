def fibs(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibs(n-1)+fibs(n-2)
n=int(input())
print(fibs(n))

fib=[1,1]+n*[0]
for i in range(2,n+1):
    fib[i]=fib[i-1]+fib[i-2]
print(fib[n-1])