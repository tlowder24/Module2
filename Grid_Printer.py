#Part 1: Print Grid
x = '+' + 4 * ' -' + ' +' + 4 * ' -' + ' +' # + & - (rows)
y = '|         |         |' # vertical lines (columns)

print(x)
print(y)
print(y)
print(y)
print(y)
print(x)
print(y)
print(y)
print(y)
print(y)
print(x)


#Part 2, print grid to size n
def print_grid_2(n):
    try:
        assert n % 2 == 1
        n = int((n-1)/2)
        x = ('+' + n * ' -' + ' +' + n* ' -' + ' +')
        y = '| ' + 2 * n * ' ' + '|' + 2 * n * ' ' + ' |'
        i = 0
        print(x)
        while i < n:
            print(y)
            i += 1
        print(x)
        i = 0
        while i < n:
            print(y)
            i += 1
        print(x)
    except AssertionError:
        print("Please use an odd integer.")


print_grid_2(11)
print_grid_2(5)


# Part 3, print grid size n and column/row height m
def print_grid_3(n, m):
    x = '+' + n * (m * ' -' + ' +')
    y = n * ('| ' + 2 * m * ' ') + '|'
    j = 0
    while j < n:
        i = 0
        print(x)
        while i < m:
            print(y)
            i += 1
        j += 1
    print(x)


print_grid_3(5, 3)




