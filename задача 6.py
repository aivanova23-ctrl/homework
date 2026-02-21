def format_number(num):
    return f"{f'{num:.3f}':*^30}".replace(',','.'.replace('.',' .'))
print(format_number(123657683.5352763))