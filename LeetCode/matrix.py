def matrixReshape( mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    ret_val = []
    new = []
    if len(mat) == r:
        for m in mat:
            ret_val.append(m)
    elif len(mat) == c:
        for m in mat:
            ret_val.append([m])
    else:
        if c > r:
            for num in range(1, r+1):
                new.append([num])
            ret_val.append(new)
        elif r > c:
            for num in range(1, c + 1):
                new.append(num)
            ret_val.append(new)

    return ret_val


print(matrixReshape([[1,2],[3,4]],1,4))
print(matrixReshape([[1,2],[3,4]],2, 4))
print(matrixReshape([[1,2],[3,4]],4, 1))