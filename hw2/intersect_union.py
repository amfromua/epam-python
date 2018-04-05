def union(*args):
    result = []
    for arg in args:
        result.extend(arg)
    return list(set(result))

def intersect(*args):
    result = []
    flag = False
    for i in range(len(args[0])):
        for j in range(1,len(args)):
            flag = False
            if args[0][i] not in args[j]:
                flag = False
                break
            else:
                flag = True
        if flag:
            result.append(args[0][i])
    return result

print(union([1,2,3,4,5],[2,3,4,5,6,7],[2,3,4,222,11]))
print(intersect([1,2,3,4,5],[2,3,4,5,6,7],[2,3,4,222,11]))