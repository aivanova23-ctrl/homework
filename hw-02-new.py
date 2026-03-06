#Задача1

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

#Задача 2

def is_correct(data):
    flag=[]
    for i in range(len(data)):
        if data[i]=='(':
            flag.append(0)
        else:
            flag.append(1)
    if flag==[]:
        return True
    else:
        return False
print(is_correct("((())))("))

#Задача 3

def plus_one(nums):
    for i in range(len(nums)-1, -1,-1):
        if nums[i]<9:
            num[i]+=1
            return nums
        num[i]=0
    return [1]+[0]*len(nums)

#Задача 4

def number_of_unique_characters(data):
    sym={}
    for i in data:
        sym[i]=sym.get(i,0)+1
    return sym
data='asdfnkkjbsdff'
print(number_of_unique_characters(data))

#Задача 5

def find(data, n):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i]+data[j]==n:
                return [i,j]
print(find([1,2,3,4], 5))

def get_sum(data,n):
    left=right=0
    while left<right:
        if n>data[right]+data[left]:
            left+=1
        elif n<data[right]+data[left]:
            right-=1
        else:
            return[left,right]


#Задача 6

def format_number(num):
    return f"{f'{num:.3f}':*^30}".replace(',','.'.replace('.',' .'))
print(format_number(123657683.5352763))