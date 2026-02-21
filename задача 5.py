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