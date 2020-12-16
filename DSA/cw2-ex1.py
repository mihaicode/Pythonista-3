##
# Data structures and algorithms Coursework
# Mihai Gheorghe
# Birkbeck University, December 2020
#
#  Exercise 1: Linear time testing for restricted lists
# This function returns True is there is an element in a list A not also found in a list B
# Compare each element of A with each element of B

# Test Cases


# compare 0 to [0, 1, 2, 3, 4, 5]  1 0 0 0 0 0 # stop comparing after element match
# compare 1 to [0, 1, 2, 3, 4, 5]  0 1 0 0 0 0
# compare 2 to [0, 1, 2, 3, 4, 5]  0 0 1 0 0 0
# compare 3 to [0, 1, 2, 3, 4, 5]  0 0 0 1 0 0
# compare x to [0, 1, 2, 3, 4, 5]  0 0 0 0 0 0  # element not found
# --------------------------------------------  # return True
# compare 4 to [0, 1, 2, 3, 4, 5]  0 0 0 0 0 0
# compare 5 to [0, 1, 2, 3, 4, 5]  0 0 0 0 0 0


def main():

    A = [1, 2, 3, 4]
    B = [9, 7, 5, 3, 1, 4]

    def OddOneOut(A, B):
        for i in range(len(A)):
            counter = 0
            for j in range(len(B)):
                print('Comparing {} to {}').format(A[i], B[j])
                counter += 1
                if A[1] != B[j]:
                    continue
                if A[i] == B[j]:
                    exit
                elif counter == len(B) & & A[i] != B[j]:
                    return True
        return False

    result = OddOneOut(A, B)
    print(result)


main()
