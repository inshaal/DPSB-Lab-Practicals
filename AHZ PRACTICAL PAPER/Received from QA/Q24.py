#write a program to accept 3*3 array of integers and check whether if forms a magic square or not
 

#------------------------------------------------------------------------------INPUT----------------------------------------------------


def magic_square(lst):
    """
    >>> magic_square([[2,7,6],[9,5,1],[4,3,8]])
    True
    """

    rows,cols,dia = [0,0,0],[0,0,0],[0,0]  #for making the default matrix
    
    for i in range(len(lst)):
        rows[i] = sum(lst[i])
        
        for j in range(len(lst[i])):
            cols[j] += lst[i][j]
            if i == j:
                dia[0] += lst[i][j]       #to check whether it forms a cube or not
            if i+j == 2:
                dia[1] += lst[i][j]
                
    print len(set(rows+cols+dia)) <= 1    #results to be true if the condition is satisfied
    
a=magic_square([[2,7,6],[9,5,1],[4,3,7]])
#------------------------------------------------------------------------OUPUT----------------------------------------------------------

#output:false,it does not form a magic cube
