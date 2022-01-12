def odd_elements(lst):
    odd_elements = []
    for index, value in enumerate(lst):
        if index % 2 == 1:
            odd_elements.append(value)
        elif value % 2 == 1:
            odd_elements.append(value)
    print(odd_elements)
    

odd_elements([1, 3, 5])