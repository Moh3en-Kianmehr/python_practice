def checkArray(array):
    if len(array) == 1: #==> check len of array
        return True
    x = 0
    flag = True
    for i in array:
        if i>=x:
            flag = True
        else:
            flag = False
        x = i
    return flag


print(checkArray([1]))