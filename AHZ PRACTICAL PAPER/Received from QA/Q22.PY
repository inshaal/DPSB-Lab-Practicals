  """
    Checks if a given 3x3 array forms a magic square.
    """

def is_magic_sqr(array):
   
    rows, cols, diag = [0] * 3, [0] * 3, [0] * 2
    for i in range(len(array)):
        for j in range(len(array[i])):
            # check rows
            rows[i] += array[i][j]
            # check cols
            cols[j] += array[i][j]
            # check diag
            if i == j:
                diag[0] += array[i][j]
            if i + j == 2:
                diag[1] += array[i][j]
    if len(set(rows + cols + diag)) == 1:
        return "The given array forms a magic square !!"
    else:
        return "The given array does not form a magic square !!"

input_array = input("Enter a 3x3 array of integers: ")
print is_magic_sqr(input_array)

"""
#OUTPUT:
Input: [[1, 3, 2], [4, 7, 9], [5, 8, 6]]
Output: The given array does not form a magic square !!

Input: [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
Output: The given array forms a magic square !!
"""
