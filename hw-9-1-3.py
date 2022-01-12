# Yongdong Xi
def find_things(str):
    not_exist = 0
    things = input("Which substring or element need to be found? ")
    for index, thing in enumerate(str):
        if things != thing:
            not_exist += 1
            continue
        if not_exist == (len(str) + 1):
            print("-1")
            break
        if things == thing:
            print(index)
            print(not_exist)
            break
        

find_things("233")
