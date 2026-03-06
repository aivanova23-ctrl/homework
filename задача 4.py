def number_of_unique_characters(data):
    sym={}
    for i in data:
        sym[i]=sym.get(i,0)+1
    return sym
data='asdfnkkjbsdff'
print(number_of_unique_characters(data))

