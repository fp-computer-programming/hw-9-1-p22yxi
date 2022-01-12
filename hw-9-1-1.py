# Yongdong Xi
def even_numbered_indexes(lst):
    even_numbered_indexes = []
    for index, value in enumerate(lst):
        if index % 2 == 0:
            even_numbered_indexes.append(value)
    print(even_numbered_indexes)
    

even_numbered_indexes(["as", 'ad', 'qw'])
