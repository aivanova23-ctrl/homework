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
