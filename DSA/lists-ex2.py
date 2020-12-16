# Check if x is contained in a list A [ExistEven(A)]
# Suppose that we want to write a function that would return true if A contains at least one even element. 
# Otherwise the function would return false
#
#
# Mihai Gheorghe
# Birkbeck University
# 2019
A = [1, 2, 3, 4, 'letters', True, -1]
B = [10, 20, 30.1, 40]
C = ["hello", 2.0, 5, [10, 20]]
D = ["spam", "bungee", "swallow"]
E = [[0,0],[0,1],[1,0]]


def ExistEven(A):
    for i in range(0, len(A)):
        if(A[i] % 2 == 0):
                
            print("Even element found".A[i])
            return True
    return False

ExistEven(A)
ExistEven(B)
ExistEven(C)
ExistEven(D)
ExistEven(E)