
def pascals_triangle(num):
    if num <= 2:
        return [[1]] if num == 1 else [[1], [1, 1]]

    result = pascals_triangle(num-1)
    last_row = list(result[len(result)-1])
    row = [1]

    for i in range(0, len(last_row)-1):
        row.append(last_row[i]+last_row[i+1])
    row.append(1)
    result.append(list(row))
    return result


triangle = pascals_triangle(5)
for row in triangle:
    print(row)
