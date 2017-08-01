def toh(n):
    if n==1:
        return 1
    else:
        return 2*toh(n-1)+1
n=input()
print toh(n)
