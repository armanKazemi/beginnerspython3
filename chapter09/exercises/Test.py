
def pascals_triangle(num):
    if num <= 2:
        return [[1]] if num == 1 else [[1], [1, 1]]

    temple = pascals_triangle(num-1)
    temple2 = list(temple[len(temple)-1])
    result = [1]

    for i in range(0, len(temple2)-1):
        result.append(temple2[i]+temple2[i+1])
    result.append(1)
    temple.append(list(result))
    return temple


triangle = pascals_triangle(5)
for row in triangle:
    print(row)